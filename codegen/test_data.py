"""Module for testing the proto data reader."""
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest
import mock

import data


class TestDataMethods(unittest.TestCase):
    """Test the proto parsing and data reading."""

    @mock.patch("data.open")
    def test_parse_can_message_enum_invalid_can_id(self, mock_open):  # pylint: disable=invalid-name
        """Tests for an invalid CAN ID handler."""
        ascii_protobuf = """
            msg {
                id:300
                msg_name: "can id over 128"
                can_data {
                    frame {
                        type: UINT64
                    }
                }
            }
        """
        mock_open.side_effect = [
            mock.mock_open(read_data=ascii_protobuf).return_value
        ]
        with self.assertRaises(Exception):
            data.parse_can_message_enum(None)

    @mock.patch("data.open")
    def test_parse_can_message_enum_duplicate_can_id(self, mock_open):  # pylint: disable=invalid-name
        """Tests there is a check for a duplicate CAN ID."""
        ascii_protobuf = """
            msg {
                id:1
                msg_name: "can message 1"
                can_data {
                    frame {
                        type: UINT64
                    }
                }
            }

            msg {
                id:1
                msg_name: "silly duplicate message id"
                can_data {
                    frame {
                        type: UINT64
                    }
                }
            }
        """
        mock_open.side_effect = [
            mock.mock_open(read_data=ascii_protobuf).return_value
        ]
        with self.assertRaises(Exception):
            data.parse_can_message_enum(None)

    @mock.patch("data.open")
    def test_parse_can_message_enum_duplicate_name(self, mock_open):  # pylint: disable=invalid-name
        """Checks for a duplicate CAN message name."""
        ascii_protobuf = """
            msg {
                id:1
                msg_name: "some name"
                can_data {
                    frame {
                        type: UINT64
                    }
                }
            }

            msg {
                id:3
                msg_name: "some name"
                can_data {
                    frame {
                        type: UINT64
                    }
                }
            }
        """
        mock_open.side_effect = [
            mock.mock_open(read_data=ascii_protobuf).return_value
        ]
        with self.assertRaises(Exception):
            data.parse_can_message_enum(None)


if __name__ == '__main__':
    unittest.main()
