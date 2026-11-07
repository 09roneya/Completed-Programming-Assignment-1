"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count("InStaNcE"), 3)

    def test_vowel_count_empty_string(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(hw1.short_lists([ [3,4,5,6], [5], [3,4], [], [], [8, 10] ]), [[3,4],[8,10]]) 

    def test_short_lists_no_matching_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(hw1.short_lists([ [6,7,8], [5,4,3,7,8], [6]]), [])
                         
    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs ([ [5,4], [10,9], [6,7], [2,3]]), [ [4,5], [9,10],[6,7], [2,3]] )

    def test_ascending_pairs_other_lengths_unchanged(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs([[5,6,7], [6,5,4], [5,4]]), [[5,6,7], [6,5,4], [4,5]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices( data.Price(4,25), data.Price(2,34)), data.Price(6,59))
    def test_add_prices_with_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices( data.Price(5,99), data.Price(10,99)), data.Price(16,98))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        rectangle  = data.Rectangle(data.Point(0,4), data.Point(5,0))
        self.assertEqual(hw1.rectangle_area(rectangle), 20)
    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        rectangle2 = data.Rectangle(data.Point(-3,4), data.Point(1, 2))
        self.assertEqual(hw1.rectangle_area(rectangle2), 8)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        book1 = data.Book(["jake", "rose"], "title1")
        book2 = data.Book(["jake"], "title2")
        book3 = data.Book(["rose"], "title3")
        self.assertEqual(hw1.books_by_author("jake", [book1, book2, book3]), [book1,book2])

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        book1 = data.Book(["jake"], "title1")
        book2 = data.Book(["jake"], "title2")
        book3 = data.Book(["rose"], "title3")
        self.assertEqual(hw1.books_by_author("maddie", [book1, book2, book3]), [])
       
    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.

        rectangle4 = data.Rectangle(data.Point(0,4), data.Point(4,0))
        self.assertEqual(hw1.circle_bound(rectangle4), data.Circle( data.Point(2.0,2.0), 8.0 ** 0.5))
    def test_circle_bound_non_square_rectangle(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        rectangle3 = data.Rectangle(data.Point(0,4), data.Point( 5,0))
        self.assertEqual(hw1.circle_bound(rectangle3), data.Circle( data.Point(2.5, 2.0), (41.0 ** 0.5) /2))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.assertEqual(hw1.below_pay_average( [(data.Employee("jake", 56)),(data.Employee("lily",98)), (data.Employee("rose", 32))]), ["jake","rose"] )
    def test_below_pay_average_empty_list(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.assertEqual(hw1.below_pay_average([]), [] )

if __name__ == '__main__':
    unittest.main()
