import os
from src.file_random_line import FileRandomLine
from unittest import TestCase

test_path = os.path.dirname(os.path.realpath(__file__))

test_one_line_file_name = test_path + "/one_line_file_for_test.txt"
test_empty_file_name = test_path + "/empty_file_for_test.txt"
test_file_name = test_path + "/file_for_test.txt"


class TestFileRandomLine(TestCase):
    
    def test_create_get_file_random_line_should_work(self):
        test_file = open(test_file_name)
        file_sorter = FileRandomLine(test_file)
        
        self.assertIsInstance(file_sorter, FileRandomLine)
        
        test_file.close()
        
    def test_get_file_random_line_should_return_sorted_value(self):
        test_file = open(test_file_name)
        file_sorter = FileRandomLine(test_file)
        sorted_value = file_sorter.get_file_random_line()
                        
        self.assertIsNotNone(sorted_value)
        
        test_file.close()
    
    def test_create_get_file_random_line_without_a_file_should_thrown_an_exception(self):
        with self.assertRaises(Exception):
            file_sorter = FileRandomLine()
    
    def test_create_get_file_random_line_with_empty_file_should_throw_an_exception(self):
        with self.assertRaises(Exception):
            empty_file = open(test_empty_file_name)
            file_sorter = FileRandomLine(empty_file)
    
    def test_file_with_one_line_should_work(self):
        one_line_file = open(test_one_line_file_name)        
        
        file_sorter = FileRandomLine(one_line_file)
        sorted_value = file_sorter.get_file_random_line()
        self.assertIsNotNone(sorted_value)
        
        one_line_file.close()
