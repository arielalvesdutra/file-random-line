import os
from src.file_value_sorter import FileValueSorter
from unittest import TestCase

test_path = os.path.dirname(os.path.realpath(__file__))

test_one_line_file_name = test_path + "/one_line_file_for_test.txt"
test_empty_file_name = test_path + "/empty_file_for_test.txt"
test_file_name = test_path + "/file_for_test.txt"


class TestFileValueSorter(TestCase):
    
    def test_create_file_value_sorter_should_work(self):
        test_file = open(test_file_name)
        file_sorter = FileValueSorter(test_file)
        
        self.assertIsInstance(file_sorter, FileValueSorter)
        
        test_file.close()
        
    def test_file_value_sorter_should_return_sorted_value(self):
        test_file = open(test_file_name)
        file_sorter = FileValueSorter(test_file)
        sorted_value = file_sorter.sort_file_value()
                        
        self.assertIsNotNone(sorted_value)
        
        test_file.close()
    
    def test_create_file_value_sorter_without_a_file_should_thrown_an_exception(self):
        with self.assertRaises(Exception):
            file_sorter = FileValueSorter()
    
    def test_create_file_value_sorter_with_empty_file_should_throw_an_exception(self):
        with self.assertRaises(Exception):
            empty_file = open(test_empty_file_name)
            file_sorter = FileValueSorter(empty_file)
    
    def test_file_with_one_line_should_work(self):
        one_line_file = open(test_one_line_file_name)        
        
        file_sorter = FileValueSorter(one_line_file)
        sorted_value = file_sorter.sort_file_value()
        self.assertIsNotNone(sorted_value)
        
        one_line_file.close()
