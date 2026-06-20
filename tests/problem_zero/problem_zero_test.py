from collections import defaultdict
from problems.problem_zero import is_square_num, get_prime_factors

"""
`is_square_num` unit tests
"""


def test_is_squares_number_should_validate_a_valid_square_number_correctly():
    # arrange

    # act
    result = is_square_num(4)

    # assert
    assert result == True


def test_is_squares_number_should_validate_non_square_numbers_correctly():
    # arrange

    # act
    result = is_square_num(5)

    # assert
    assert result == False


def test_is_squares_number_should_validate_one_as_valid_square_number():
    # arrange

    # act
    result = is_square_num(1)

    # assert
    assert result == True


"""
`is_square_num` integration tests
"""


def test_is_squares_number_should_validate_valid_square_numbers():
    # arrange
    valid_square_numbers = []
    is_valid_flag_freq = defaultdict(int)

    with open("./tests/problem_zero/square_numbers.txt", "r") as f:
        valid_square_numbers = [int(num) for num in f.read().split(",")]

    # act
    for valid_square_number in valid_square_numbers:
        is_valid = is_square_num(valid_square_number)
        is_valid_flag_freq[is_valid] += 1

    # assert
    assert len(is_valid_flag_freq.values()) == 1
    assert list(is_valid_flag_freq.values())[0] == 152


"""
`get_prime_factors` unit tests
"""


def test_get_prime_factors_should_return_valid_factors():
    # arrange
    expected_value = [5, 5, 5, 5]

    # act
    result = get_prime_factors(625)

    # assert
    assert result == expected_value


def test_get_prime_factors_should_return_empty_list_for_one():
    # arrange
    expected_value = []

    # act
    result = get_prime_factors(1)

    # assert
    assert result == expected_value
