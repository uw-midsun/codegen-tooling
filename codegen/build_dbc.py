"""
This script generates a DBC file from our custom protobufs in order to make the
transition to DBCs more seamless. This is a temporary measure so we can
continue to use codegen-tooling, while switching over to using DBC decoders so
we do not have to maintain the dump scripts.

The idea is that we will eventually switch over to DBC files, or a higher level
DSL that compiles down into DBC files (ie. if our CAN protocol changes).
"""
import cantools

# For the proto and asciipb parsing
import data

def build_arbitration_id(msg_type, source_id, msg_id):
    """
    typedef union CanId {
      uint16_t raw;
      struct {
        uint16_t source_id : 4;
        uint16_t type : 1;
        uint16_t msg_id : 6;
      };
    } CanId;
    """
    return ((source_id & ((0x1 << 4) - 1)) << (0)) | \
            ((msg_type & ((0x1 << 1) - 1)) << (4)) | \
            ((msg_id & ((0x1 << 6) - 1)) << (4 + 1))

def main():
    db = cantools.database.can.Database(version='')

    # Iterate through all the CAN device IDs and add them to the DBC.
    can_devices = data.parse_can_device_enum()
    for device_id, device_name in can_devices.items():
        if device_name not in [ 'RESERVED' ]:
            node = cantools.database.can.Node(
                name=device_name,
                comment='Device ID: {}'.format(hex(device_id))
            )
            db.nodes.append(node)

    # Iterate through all the CAN messages IDs and:
    #
    #   1. Convert the Message ID to the CAN Arbitration ID.
    #   2. Add the Message to the DBC.
    #   3. For each of the signals, add it to the Message.
    #   4. If the Message is critical, add an ACK message to the DBC.
    can_messages = data.parse_can_frames('can_messages.asciipb')
    device_enum = data.parse_can_device_enum()


    FIELDS_LEN = { 'u8': 8, 'u16': 16, 'u32': 32, 'u64': 64 }
    def get_key_by_val(d, val):
        for k, v in d.items():
            if val == v:
                return k
        return None

    for msg_id, can_frame in can_messages.items():
        source = get_key_by_val(device_enum, can_frame.source)

        def get_muxed_voltage_signal():
            """
            Get the MUXed signals for the Voltage V/T message.
            """
            # The MUX'd message is formatted like this:
            #
            #  16-bits   16-bits     16-bits
            # +--------+---------+-------------+
            # |   id   | voltage | temperature |
            # +--------+---------+-------------+
            #
            # due to CANdlelight 1.0 alignment rules.
            results = []
            # Generate the signal used as the multiplexer
            # TODO: This is kind of a hack, but idk
            multiplexer = cantools.database.can.Signal(
                 name='BATTERY_VT_INDEX',
                 start=0,
                 length=16,
                 byte_order='little_endian',
                 is_signed=False,
                 scale=1,
                 offset=0,
                 minimum=None,
                 maximum=None,
                 unit=None,
                 choices=None,
                 dbc_specifics=None,
                 comment=None,
                 receivers=None,
                 is_multiplexer=True,
                 multiplexer_ids=None,
                 multiplexer_signal=None,
                 is_float=False,
                 decimal=None)
            results.append(multiplexer)

            # TODO: This range should probably be moved to a constant or
            # something...
            # Generate all the multiplexed signals
            for i in range(0, 36):
                # The voltage is the second field
                voltage = cantools.database.can.Signal(
                    name='CELL_VOLTAGE_{0:03d}'.format(i),
                    start=16,
                    length=16,
                    byte_order='little_endian',
                    is_signed=False,
                    scale=1,
                    offset=0,
                    minimum=None,
                    maximum=None,
                    unit=None,
                    choices=None,
                    dbc_specifics=None,
                    comment=None,
                    receivers=None,
                    is_multiplexer=False,
                    # The multiplexed ID is just the Cell Index
                    multiplexer_ids=[i],
                    multiplexer_signal=results[0],
                    is_float=False,
                    decimal=None
                )

                temperature = cantools.database.can.Signal(
                    name='CELL_TEMP_{0:03d}'.format(i),
                    start=32,
                    length=16,
                    byte_order='little_endian',
                    is_signed=False,
                    scale=1,
                    offset=0,
                    minimum=None,
                    maximum=None,
                    unit=None,
                    choices=None,
                    dbc_specifics=None,
                    comment=None,
                    receivers=None,
                    is_multiplexer=False,
                    # The multiplexed ID is just the Cell Index
                    multiplexer_ids=[i],
                    multiplexer_signal=results[0],
                    is_float=False,
                    decimal=None
                )

                results.append(voltage)
                results.append(temperature)

            return results

        # TODO: iirc, only ACKs have DLC 0, otherwise everything else has a
        # DLC of 8. Check this tho
        #
        # All these message types must be Data messages. ACK messages are
        # currently handled implicitly by the protocol layer, and will be
        # generated based on whether or not it is an ACKable message.
        frame_id = build_arbitration_id(
            msg_type=0,
            source_id=source,
            msg_id=msg_id
        )
        print(can_frame.msg_name)
        if can_frame.msg_name == 'BATTERY_VT':
            signals = get_muxed_voltage_signal()

            # TODO: fix length
            # It is safe to divide by 8 since every single message under the old
            # protocol (aka. what I call CANdlelight 1.0) is byte-aligned. To be
            # precise, it uses byte-alignment padding to fit 8, 4, 2, 1 bytes.
            message = cantools.database.can.Message(
                frame_id=frame_id,
                name=can_frame.msg_name,
                length=6,
                signals=signals,
                # The sender is the Message Source
                senders=[can_frame.source]
            )
            db.messages.append(message)
        else:
            # TODO: hack
            total_length = 0
            signals = []
            for index, field in enumerate(can_frame.fields):
                length = FIELDS_LEN[can_frame.ftype]

                # Unfortunately, our asciipb doesn't denote whether a field is
                # signed/unsigned, and it is up to the caller to properly unpack
                # the CAN signal.
                #
                # In this case, it's probably easier to just assume everything is
                # unsigned and then force people to make a manual pass through and
                # mark things as appropriate.
                #
                # TBH, we only have a few signals that are signed.
                signal = cantools.database.can.Signal(
                    name=field,
                    start=index*length,
                    length=length,
                    byte_order='little_endian',
                    is_signed=False,
                    scale=1,
                    offset=0,
                    is_float=False
                )
                signals.append(signal)
                total_length += length

            # TODO: fix length
            # It is safe to divide by 8 since every single message under the old
            # protocol (aka. what I call CANdlelight 1.0) is byte-aligned. To be
            # precise, it uses byte-alignment padding to fit 8, 4, 2, 1 bytes.
            message = cantools.database.can.Message(
                frame_id=frame_id,
                name=can_frame.msg_name,
                length=total_length // 8,
                signals=signals,
                # The sender is the Message Source
                senders=[can_frame.source]
            )
            db.messages.append(message)

            # If this requires an ACK, then we go through all of the receivers.
            # Unfortunately, our asciipb file doesn't have a notion of Receivers,
            # so we hardcode this.
            ACKABLE_MESSAGES = {
                0: [
                    'CHAOS',
                    'LIGHTS_FRONT',
                    'PLUTUS_SLAVE',
                    'DRIVER_CONTROLS'
                ],
                1: [
                    'DRIVER_CONTROLS'
                ],
                2: [
                    'PLUTUS'
                ],
                3: [
                    'PLUTUS_SLAVE'
                ],
                4: [
                    'MOTOR_CONTROLLER'
                ],
                5: [
                    'SOLAR_MASTER_REAR'
                ],
                6: [
                    'SOLAR_MASTER_FRONT'
                ],
                7: [
                    'CHAOS'
                ],
                8: [
                    'PLUTUS',
                    'MOTOR_CONTROLLER',
                    'DRIVER_CONTROLS'
                ],
            }

        def get_ack(sender, msg_name, msg_id):
            """
            msg_id: the id of the message we are ACKing
            """
            sender_id = get_key_by_val(device_enum, sender)
            if sender_id is None:
                print("Couldn't find {}".format(sender))

            frame_id = build_arbitration_id(
                msg_type=1,
                source_id=sender_id,
                msg_id=msg_id
            )

            # TODO: ack_status
            signals = [
                cantools.database.can.Signal(
                    name='{}_from_{}_ack_status'.format(msg_name, sender),
                    start=0,
                    length=8,
                    byte_order='little_endian',
                    is_signed=False,
                    scale=1,
                    offset=0,
                    is_float=False
                )
            ]
            # TODO: properly calculate length calculation
            message = cantools.database.can.Message(
                frame_id=frame_id,
                name='{}_ACK_FROM_{}'.format(msg_name, sender),
                length=1,
                signals=signals,
                # The sender is the Message Source
                senders=[sender]
            )
            return message

        if msg_id in ACKABLE_MESSAGES:
            for acker in ACKABLE_MESSAGES[msg_id]:
                message = get_ack(acker, can_frame.msg_name, msg_id)

                db.messages.append(message)

    # Save as a DBC file
    with open('test.dbc', 'w') as f:
        f.write(db.as_dbc_string())
    return

if __name__ == '__main__':
    main()
