# pylint: disable=import-error
"""Module used for testing of pagination_generator method"""
from unittest import TestCase
import random
from pagination_gen import pagination_generator as pg

class TestPaginationGenerator(TestCase):
    """Class with tests targetting the pagination_generator method"""

    def test_float_values(self):
        """Test that TypeError is raised when input values are type float"""
        test_float=random.random()
        self.assertRaises(TypeError, pg, test_float, 2, 2, 2)
        self.assertRaises(TypeError, pg, 2, test_float, 2, 2)
        self.assertRaises(TypeError, pg, 2, 2, test_float, 2)
        self.assertRaises(TypeError, pg, 2, 2, 2, test_float)

    def test_boolean_values(self):
        """Test that TypeError is raised when input values are type boolean"""
        test_boolean=random.choice([True,False])
        self.assertRaises(TypeError, pg, test_boolean, 2, 2, 2)
        self.assertRaises(TypeError, pg, 2, test_boolean, 2, 2)
        self.assertRaises(TypeError, pg, 2, 2, test_boolean, 2)
        self.assertRaises(TypeError, pg, 2, 2, 2, test_boolean)

    def test_string_values(self):
        """Test that TypeError is raised when input values are type string"""
        test_string='test'
        self.assertRaises(TypeError, pg, test_string, 2, 2, 2)
        self.assertRaises(TypeError, pg, 2, test_string, 2, 2)
        self.assertRaises(TypeError, pg, 2, 2, test_string, 2)
        self.assertRaises(TypeError, pg, 2, 2, 2, test_string)

    def test_null_values(self):
        """Test that TypeError is raised when input values are type null"""
        self.assertRaises(TypeError, pg, None, 2, 2, 2)
        self.assertRaises(TypeError, pg, 2, None, 2, 2)
        self.assertRaises(TypeError, pg, 2, 2, None, 2)
        self.assertRaises(TypeError, pg, 2, 2, 2, None)

    def test_dict_values(self):
        """Test that TypeError is raised when input values are type dict"""
        test_dict={'key':1}
        self.assertRaises(TypeError, pg, test_dict, 2, 2, 2)
        self.assertRaises(TypeError, pg, 2, test_dict, 2, 2)
        self.assertRaises(TypeError, pg, 2, 2, test_dict, 2)
        self.assertRaises(TypeError, pg, 2, 2, 2, test_dict)

    def test_list_values(self):
        """Test that TypeError is raised when input values are type list"""
        test_list=[0,1,2]
        self.assertRaises(TypeError, pg, test_list, 2, 2, 2)
        self.assertRaises(TypeError, pg, 2, test_list, 2, 2)
        self.assertRaises(TypeError, pg, 2, 2, test_list, 2)
        self.assertRaises(TypeError, pg, 2, 2, 2, test_list)

    def test_set_values(self):
        """Test that TypeError is raised when input values are type set"""
        test_set={0,1,2}
        self.assertRaises(TypeError, pg, test_set, 2, 2, 2)
        self.assertRaises(TypeError, pg, 2, test_set, 2, 2)
        self.assertRaises(TypeError, pg, 2, 2, test_set, 2)
        self.assertRaises(TypeError, pg, 2, 2, 2, test_set)

    def test_zero_values(self):
        """Test that ValueError is raised when input values are zero"""
        self.assertRaises(ValueError, pg, 0, 2, 2, 2)
        self.assertRaises(ValueError, pg, 2, 0, 2, 2)
        self.assertRaises(ValueError, pg, 2, 2, 0, 2)

    def test_negative_values(self):
        """Test that ValueError is raised when input values are negative"""
        test_negative = -random.randint(1,100)
        self.assertRaises(ValueError, pg, test_negative, 2, 2, 2)
        self.assertRaises(ValueError, pg, 2, test_negative, 2, 2)
        self.assertRaises(ValueError, pg, 2, 2, test_negative, 2)
        self.assertRaises(ValueError, pg, 2, 2, 2, test_negative)

    def test_boundaries_higher_than_total_pages(self):
        """Test that ValueError is raised when boundaries are higher than total pages"""
        self.assertRaises(ValueError, pg, 2, 2, 3, 2)

    def test_current_page_higher_than_total_pages(self):
        """Test that ValueError is raised when current page is higher than total pages"""
        self.assertRaises(ValueError, pg, 3, 2, 2, 2)

    def test_around_higher_than_total_pages(self):
        """Test that ValueError is raised when around is higher than total pages"""
        self.assertRaises(ValueError, pg, 2, 2, 2, 3)

    def test_valid_full_list(self):
        """Test that the output is the correct string given the input values"""
        self.assertEqual(pg(4,5,5,0), '1 2 3 4 5')
        self.assertEqual(pg(4,5,1,5), '1 2 3 4 5')
        self.assertEqual(pg(4,5,5,5), '1 2 3 4 5')
        self.assertEqual(pg(2,5,3,0), '1 2 3 4 5')
        self.assertEqual(pg(4,5,1,2), '1 2 3 4 5')
        self.assertEqual(pg(2,3,1,0), '1 2 3')
        self.assertEqual(pg(1,3,1,1), '1 2 3')

    def test_valid_list_with_dots(self):
        """"Tests which output lists with '...' inside"""
        self.assertEqual(pg(4,5,1,0), '1 ... 4 5')
        self.assertEqual(pg(2,5,2,0), '1 2 ... 4 5')
        self.assertEqual(pg(4,10,2,2), '1 2 3 4 5 6 ... 9 10')
        self.assertEqual(pg(4,10,1,1), '1 ... 3 4 5 ... 10')
        self.assertEqual(pg(5,10,2,1), '1 2 ... 4 5 6 ... 9 10')
        self.assertEqual(pg(500,1000,2,1), '1 2 ... 499 500 501 ... 999 1000')
