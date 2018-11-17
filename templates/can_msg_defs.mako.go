<%namespace name="helpers" file="/helpers/helpers.mako" /> \
<% from data import NUM_CAN_MESSAGES, NUM_CAN_DEVICES, parse_can_device_enum, parse_can_message_enum, parse_can_frames %> \
package CanMsgDefs

type CanDeviceId uint16
type CanMsgId uint32

// For setting the CAN device
const (
  <% can_devices = parse_can_device_enum() %> \
${helpers.generate_enum_go(can_devices, 'SystemCanDevice', 'CanDeviceId')}
)  

// For setting the CAN message ID
const (
  <% can_messages = parse_can_message_enum(options.filename) %> \
${helpers.generate_enum_go(can_messages, 'SystemCanMessage', 'CanMsgId')}
)
