import unittest
from constants import *
from life_logger_utils import *
from data_types.did_do import *
from data_types.key_event import *
from data_types.note import *
from data_types.state_change import *
from data_types.time import *
from data_types.value import *

# TODO: breaks up tests and write more

class Logger_Tests(unittest.TestCase): 
  
    def test_comments_simple(self):
        line = constants.COMMENT_OUT_STRING + "hello"
        self.assertTrue(is_line_commented(line))

    def test_comments_empty(self):
        line = ""
        self.assertTrue(not is_line_commented(line))

    def test_comments_after(self):
        line = "v{}stuff".format(constants.COMMENT_OUT_STRING)
        self.assertTrue(not is_line_commented(line))

    def test_get_value_label0(self):
        definition = "(0,8) e"
        self.assertEqual("e", get_value_label(definition))

    def test_get_value_label1(self):
        definition = "(3,20) name_here"
        self.assertEqual("name_here", get_value_label(definition))

    def test_get_value_range_simple(self):
        definition = "(0,8) e"
        self.assertEqual((0,8), get_value_range(definition))

    def test_get_value_range_two_char_numbers(self):
        definition = "(3,20) name_here"
        self.assertEqual((3,20), get_value_range(definition))

    def testis_valid_value_valid_low(self):
        self.assertTrue(is_valid_value("5",5, 10))

    def testis_valid_value_valid_high(self):
        self.assertTrue(is_valid_value("9",5, 10))

    def testis_valid_value_invalid_low(self):
        self.assertTrue(not is_valid_value("4",5, 10))

    def testis_valid_value_invalid_high(self):
        self.assertTrue(not is_valid_value("10",5, 10))

    def testis_valid_value_valid_not_a_number(self):
        self.assertTrue(not is_valid_value("8s",5, 10))

if __name__ == '__main__': 
    unittest.main() 