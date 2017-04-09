"""Parsing and data-related functions
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import can_pb2
import validator

from google.protobuf import text_format

import re
from constants import NUM_CAN_DEVICES, NUM_CAN_MESSAGES


def read_protobuf_data(filename):
    """Reads and parses the specified ASCII Pb

    Args:
        filename: a string representing the filename to read

    Returns:
        a list of Pb values
    """
    can_messages = can_pb2.CanSchema()
    with open(filename, 'r') as asciipb:
        text_format.Merge(asciipb.read(), can_messages)
    return can_messages.msg


def parse_can_device_enum():
    """Read and parse the CanMsg source devices

    Args:
        None

    Returns:
        a dictionary of CAN source devices and their names
    """
    can_devices = {}
    for key in range(NUM_CAN_DEVICES):
        can_devices[key] = None
    for name, value in can_pb2.CanMsg.Source.items():
        can_devices[value] = name
    return can_devices


def parse_can_message_enum():
    """Parses CAN messages into dictionary
    """
    messages = {}
    for i in range(128):
        messages[i] = None
    can_messages = read_protobuf_data('can_messages.asciipb') # todo change
    for can_message in can_messages:
        if validator.valid_can_id(can_message.id) == False:
            raise Exception('Invalid CAN id')
        if messages[can_message.id] == None:
            messages[can_message.id] = to_identifier(can_message.msg_name)
        else:
            raise Exception('Duplicate CAN id %s' % can_message.id)
    return messages


def to_identifier(name):
    """Convert name to an identifier (upper snake case)

    Args:
        string: a string to be converted to an identifier

    Returns:
        a string in snake case
    """
    name = name.replace(' ', '_')
    return name.upper()
