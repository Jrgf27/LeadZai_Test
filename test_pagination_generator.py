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

    def test_invalid_zero_values(self):
        """Test that ValueError is raised when input values are zero"""
        self.assertRaises(ValueError, pg, 0, 2, 2, 2)
        self.assertRaises(ValueError, pg, 2, 0, 2, 2)

    def test_negative_values(self):
        """Test that ValueError is raised when input values are negative"""
        test_negative = -random.randint(1,100)
        self.assertRaises(ValueError, pg, test_negative, 2, 2, 2)
        self.assertRaises(ValueError, pg, 2, test_negative, 2, 2)
        self.assertRaises(ValueError, pg, 2, 2, test_negative, 2)
        self.assertRaises(ValueError, pg, 2, 2, 2, test_negative)

    def test_current_page_higher_than_total_pages(self):
        """Test that ValueError is raised when current page is higher than total pages"""
        self.assertRaises(ValueError, pg, 3, 2, 2, 2)

    def test_valid_full_list_current_page_at_end(self):
        """Test with valid values and current page at the end of pagination"""
        self.assertEqual(pg(5,5,5,0), '1 2 3 4 5')
        self.assertEqual(pg(4,5,1,5), '1 2 3 4 5')
        self.assertEqual(pg(3,3,1,1), '1 2 3')

    def test_valid_full_list_current_page_at_start(self):
        """Test with valid values and current page at the start of pagination"""
        self.assertEqual(pg(2,5,3,0), '1 2 3 4 5')
        self.assertEqual(pg(1,3,1,1), '1 2 3')

    def test_valid_full_list_around_value_zero(self):
        """Test with valid values and around value as zero"""
        self.assertEqual(pg(5,5,5,0), '1 2 3 4 5')
        self.assertEqual(pg(5,5,3,0), '1 2 3 4 5')
        self.assertEqual(pg(1,3,2,0), '1 2 3')

    def test_valid_full_list_around_large_value(self):
        """Test with valid values and around value as a large integer"""
        self.assertEqual(pg(5,5,1,1000), '1 2 3 4 5')
        self.assertEqual(pg(1,3,1,1000), '1 2 3')

    def test_valid_full_list_boundaries_value_zero(self):
        """Test with valid values and boundaries value as zero"""
        self.assertEqual(pg(5,5,0,5), '1 2 3 4 5')
        self.assertEqual(pg(1,3,0,3), '1 2 3')

    def test_valid_full_list_boundaries_large_value(self):
        """Test with valid values and boundaries value as a large integer"""
        self.assertEqual(pg(5,5,1000,0), '1 2 3 4 5')
        self.assertEqual(pg(1,3,1000,0), '1 2 3')

    def test_valid_list_with_dots_current_page_at_end(self):
        """"Tests which output lists with '...' inside and current page at end of list"""
        self.assertEqual(pg(4,5,1,0), '1 ... 4 5')
        self.assertEqual(pg(4,10,2,2), '1 2 3 4 5 6 ... 9 10')

        self.assertEqual(pg(10,10,3,1), '1 2 3 ... 8 9 10')
        self.assertEqual(pg(9,10,4,1), '1 2 3 4 ... 7 8 9 10')

    def test_valid_list_with_dots_current_page_at_start(self):
        """"Tests which output lists with '...' inside and current page at start of list"""
        self.assertEqual(pg(2,5,2,0), '1 2 ... 4 5')
        self.assertEqual(pg(2,10,3,1), '1 2 3 ... 8 9 10')
        self.assertEqual(pg(1,10,4,1), '1 2 3 4 ... 7 8 9 10')

    def test_valid_list_with_dots_current_page_at_middle(self):
        """"Tests which output lists with '...' inside and current page at middle of list"""
        self.assertEqual(pg(4,10,1,1), '1 ... 3 4 5 ... 10')
        self.assertEqual(pg(5,10,2,1), '1 2 ... 4 5 6 ... 9 10')

    def test_valid_list_with_dots_large_values(self):
        """Test which outputs a valid list given large total and current pages values"""
        self.assertEqual(pg(500,1000,2,1), '1 2 ... 499 500 501 ... 999 1000')

    def test_valid_list_with_dots_around_value_zero(self):
        """Test which output lists with '...' inside and around value as zero"""
        self.assertEqual(pg(5,10,1,0), '1 ... 5 ... 10')
        self.assertEqual(pg(1,10,1,0), '1 ... 10')
        self.assertEqual(pg(2,10,1,0), '1 2 ... 10')
        self.assertEqual(pg(9,10,1,0), '1 ... 9 10')
        self.assertEqual(pg(10,10,1,0), '1 ... 10')

    def test_valid_list_with_dots_boundary_value_zero(self):
        """Test which output lists with '...' inside and boundary value as zero"""
        self.assertEqual(pg(5,10,0,0), '... 5 ...')
        self.assertEqual(pg(1,10,0,0), '1 ...')
        self.assertEqual(pg(1,10,0,2), '1 2 3 ...')
        self.assertEqual(pg(10,10,0,0), '... 10')
        self.assertEqual(pg(9,10,0,2), '... 7 8 9 10')
