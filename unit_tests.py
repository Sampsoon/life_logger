import unittest
import life_logger

class Logger_Tests(unittest.TestCase): 
  
    def test_comments_simple(self):
        line = "//hello"
        self.assertTrue(life_logger.is_line_commented(line))

    def test_comments_empty(self):
        line = ""
        self.assertTrue(not life_logger.is_line_commented(line))

    def test_comments_after(self):
        line = "v//stuff"
        self.assertTrue(not life_logger.is_line_commented(line))

    def test_comments_spaces(self):
        line = "/ /stuff"
        self.assertTrue(not life_logger.is_line_commented(line))

  
if __name__ == '__main__': 
    unittest.main() 