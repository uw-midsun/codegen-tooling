from __future__ import absolute_import, division, print_function, unicode_literals

import mock
import unittest

import data

class TestDataMethods(unittest.TestCase):
    @mock.patch("data.open")
    def test_parse_can_message_enum_invalid_can_id(self, mock_open):
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
            data.parse_can_message_enum()


    @mock.patch("data.open")
    def test_parse_can_message_enum_duplicate_can_id(self, mock_open):
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
            data.parse_can_message_enum()


    @mock.patch("data.open")
    def test_parse_can_message_enum_duplicate_name(self, mock_open):
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
            data.parse_can_message_enum()


if __name__ == '__main__':
    unittest.main()
