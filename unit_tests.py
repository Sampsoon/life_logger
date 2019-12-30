import unittest
from constants import *
from config_utils import *
from data_types.did_do import *
from data_types.key_event import *
from data_types.note import *
from data_types.state_change import *
from data_types.time import *
from data_types.range import *

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

    def test_get_range_label0(self):
        definition = "(0,8) e"
        self.assertEqual("e", get_range_label(definition))

    def test_get_range_label1(self):
        definition = "(3,20) name_here"
        self.assertEqual("name_here", get_range_label(definition))

    def test_get_bounds_simple(self):
        definition = "(0,8) e"
        self.assertEqual((0,8), get_bounds(definition))

    def test_get_bounds_two_char_numbers(self):
        definition = "(3,20) name_here"
        self.assertEqual((3,20), get_bounds(definition))

    def testis_valid_range_valid_low(self):
        self.assertTrue(is_valid_range("5",5, 10))

    def testis_valid_range_valid_high(self):
        self.assertTrue(is_valid_range("9",5, 10))

    def testis_valid_range_invalid_low(self):
        self.assertTrue(not is_valid_range("4",5, 10))

    def testis_valid_range_invalid_high(self):
        self.assertTrue(not is_valid_range("10",5, 10))

    def testis_valid_range_valid_not_a_number(self):
        self.assertTrue(not is_valid_range("8s",5, 10))
        
    def testis_valid_range_definition_none_int(self):
        self.assertTrue(not is_valid_range_definition('(87w7,10000) hello'))
        
    def testis_valid_range_definition_float(self):
        self.assertTrue(not is_valid_range_definition('(87.0,10000) hello'))
        
    def testis_valid_range_definition_no_left(self):
        self.assertTrue(not is_valid_range_definition('0,10) hello'))
        
    def testis_valid_range_definition_no_right(self):
        self.assertTrue(not is_valid_range_definition('(0,10 hello'))
        
    def testis_valid_range_definition_no_comma(self):
        self.assertTrue(not is_valid_range_definition('(110) hello'))
        
    def testis_valid_range_definition_comma_on_left(self):
        self.assertTrue(not is_valid_range_definition('(,010) hello'))
        
    def testis_valid_range_definition_comma_on_right(self):
        self.assertTrue(not is_valid_range_definition('(010,) hello'))
        
    def testis_valid_range_definition_two_comma(self):
        self.assertTrue(not is_valid_range_definition('(0,1,0) hello'))
        
    def testis_valid_range_definition_basic(self):
        self.assertTrue(is_valid_range_definition('(0,10) hello'))

if __name__ == '__main__': 
    unittest.main() 