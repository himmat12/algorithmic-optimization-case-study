from problems.problem_zero.problem_zero_optimised import generate_square_nums

"""
`generate_square_nums` unit tests
"""

def test_generate_square_nums_generates_valid_range_of_square_nums():
    # arrange
    res = []
    expected_square_nums = []
    
    with open("./tests/problem_zero/square_numbers.txt", "r") as f:
        expected_square_nums = [int(num) for num in f.read().split(",")]
    expected_count = len(expected_square_nums)

    # act
    for generated in generate_square_nums():
        num = generated[0]
        if len(res) != expected_count:
            res.append(num)    
            continue
        break
    
    # assert
    assert len(res) == expected_count
    
    for res, exp in zip(res, expected_square_nums):
        assert res == exp
