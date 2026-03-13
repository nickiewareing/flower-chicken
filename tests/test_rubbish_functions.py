from src import basic_functions


def test_return_greeting():
    assert basic_functions.return_greeting('frog') == 'Hi frog'


def test_sum():
    nums = [1, 2, 3]
    assert basic_functions.add_numbers_in_list(nums) == 6