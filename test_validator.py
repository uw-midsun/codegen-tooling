from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

import validator
from constants import NUM_CAN_MESSAGES

class TestValidatorMethods(unittest.TestCase):
    def test_valid_can_id_in_range(self):
        for can_msg_id in range(0, NUM_CAN_MESSAGES):
            self.assertTrue(validator.valid_can_id(can_msg_id))

    def test_valid_can_id_out_of_range(self):
        self.assertFalse(validator.valid_can_id(NUM_CAN_MESSAGES))
