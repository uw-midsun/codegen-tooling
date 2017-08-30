"""Parsing and data-related functions
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import os

from collections import defaultdict

from constants import NUM_CAN_DEVICES, NUM_CAN_MESSAGES  # pylint: disable=unused-import
from google.protobuf import text_format

import validator
sys.path.append(
    os.path.abspath(
        os.path.dirname(os.path.realpath(__file__)) + '/../genfiles'))
import can_pb2  # pylint: disable=import-error,wrong-import-position


def read_protobuf_data(filename):
    """Reads and parses the specified ASCII Pb

    Args:
        filename: a string representing the filename to read

    Returns:
        a list of Pb values
    """
    can_messages = can_pb2.CanSchema()
    try:
        with open(filename, 'r') as asciipb:
            text_format.Merge(asciipb.read(), can_messages)
    except Exception:
        raise Exception('Could not parse ASCII Protobuf file %s' % filename)
    return can_messages.msg


def parse_can_device_enum():
    """Read and parse the CanMsg source devices

    Args:
        None

    Returns:
        a dictionary of CAN source devices and their names
    """
    can_devices = defaultdict(lambda: None)
    for name, value in can_pb2.CanMsg.Source.items():
        can_devices[value] = name
    return can_devices


def parse_can_message_enum(can_messages_file):
    """Parses CAN messages into dictionary

    Args:
        string: a string with the CAN message file name

    Returns:
        a dictionary of CAN messages
    """
    messages = defaultdict(lambda: None)
    can_messages = read_protobuf_data(can_messages_file)
    for can_message in can_messages:
        identifier = to_identifier(can_message.msg_name)
        if validator.valid_can_id(can_message.id) is False:
            raise Exception('Invalid CAN id')
        if messages[can_message.id] != None:
            raise Exception('Duplicate CAN id %s' % can_message.id)
        if identifier in messages.values():
            raise Exception('Duplicate message name %s' % can_message.msg_name)
        messages[can_message.id] = identifier

    return messages


def to_identifier(name):
    """Convert name to an identifier (upper snake case)

    Args:
        string: a string to be converted to an identifier

    Returns:
        a string in snake case
    """
    return name.replace(' ', '_').upper()
