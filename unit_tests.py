import unittest
import life_logger
import constants

class Logger_Tests(unittest.TestCase): 
  
    def test_comments_simple(self):
        line = constants.COMMENT_OUT_STRING + "hello"
        self.assertTrue(life_logger.is_line_commented(line))

    def test_comments_empty(self):
        line = ""
        self.assertTrue(not life_logger.is_line_commented(line))

    def test_comments_after(self):
        line = "v{}stuff".format(constants.COMMENT_OUT_STRING)
        self.assertTrue(not life_logger.is_line_commented(line))
  
if __name__ == '__main__': 
    unittest.main() 