import sys
sys.path.append("..")

from problems.basic import *
import pytest

class TestBasic:
    
    def test_print_hello_world(self):
        assert print_hello_world() == "Hello World!", "Must return Hello World!"
    
    def test_add_two_and_four(self):
        assert add_two_and_four() == 6, "2 + 4 == 6"

    def test_add_two_numbers(self):
        # Valid numbers
        assert add_two_numbers(2, 3) == 5, "2 + 3 == 5"
        assert add_two_numbers(100, -25) == 75, "100 + (-25) == 75"

        # Strings
        assert add_two_numbers('a', 'b') == None, "Strings shouldn't be processed"

        # Mixed types
        assert add_two_numbers('a', 2) == None, "Mixed types shouldn't be processed"
    
    def test_sum_of_list(self):
        # Valid parameters
        assert sum_of_list([2, 3, 4, 5]) == 14, "2 + 3 + 4 + 5 == 14"
        assert sum_of_list([0, 1, 10]) == 11, "0 + 1 + 10 == 11"

        # Strings
        assert sum_of_list(['a', 'b']) == None, "Strings shouldn't be processed"

        # Mixed types
        assert sum_of_list(['a', 2]) == None, "Mixed types shouldn't be processed"

    def test_number_of_words(self):
        # Valid parameters
        assert number_of_words("Hey") == 1, "'Hey' is 1 word"
        assert number_of_words("Hello World") == 2, "'Hello World' is 2 words"

        # Punctuation and numbers
        assert number_of_words("Hello World!") == 2, "'Hello World!' is 2 words"
        assert number_of_words("Hello World !") == 3, "'Hello World !' is 3 words"
        assert number_of_words("123 33!@^$n") == 2, "'123 33!@^$n' is 2 words"

        # Whitespace
        assert number_of_words("    Hello   ") == 1, "'    Hello    ' is 1 word"
        assert number_of_words("    q a   s ") == 3, "'    q a   s ' is 3 words"

    def test_multiples_of_five(self):
        # Valid parameters
        assert multiples_of_five(20) == [5, 10, 15], "Multiples of five before 20 are 5, 10, 15"
        assert multiples_of_five(12) == [5, 10], "Multiples of five before 12 are 5, 10"

        # Low numbers
        assert multiples_of_five(4) == [], "Multiples of five before 4 are none"
        assert multiples_of_five(0) == [], "Multiples of five before 0 are none"
        assert multiples_of_five(-20) == [], "Multiples of five before -20 are none"

        # Strings
        assert multiples_of_five("hey") == None, "Strings shouldn't be processed"
        assert multiples_of_five("five") == None, "Strings shouldn't be processed"

    def test_count_multiples_of_fifteen(self):
        # Valid parameters
        assert count_multiples_of_fifteen(40) == 2, "Multiples of 15 up to 40 are 2-fold"
        assert count_multiples_of_fifteen(72) == 4, "Multiples of 15 up to 72 are 4-fold"
        assert count_multiples_of_fifteen(15) == 1, "Multiples of 15 up to 15 are 1"

        # Invalid parameters
        assert count_multiples_of_fifteen("hello") == None, "Strings shouldn't be processed"
        assert count_multiples_of_fifteen([2, 3]) == None

    def test_int_dividends(self):
        # Valid parameters
        assert int_dividends(12) == [1, 2, 3, 4, 6, 12], "Integer dividends of 12: 1, 2, 3, 4, 6, 12"
        assert int_dividends(21) == [1, 3, 7, 21], "Integer dividends of 21: 1, 3, 7, 21"
        assert int_dividends(19) == [1, 19], "Integer dividends of 19: 1, 19"
        assert int_dividends(1) == [1], "Integer dividends of 1: 1"

        # Invalid parameters
        assert int_dividends(0) == [], "Zero should return empty"
        assert int_dividends(-20) == [], "Negative numbers should return empty"
        assert int_dividends("hey") == None, "Strings shouldn't be processed"