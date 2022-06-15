# LIBS
from main import main

# CONSTANTS
SET = {1, 2, 3, 4}
SET_ORDERED = [1, 2, 3, 4]
SUBSETS_LIST = [
    {1}, {2}, {3}, {4},
    {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4},
    {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4},
    {1, 2, 3, 4}
]
SUBSETS_DIVISIBLE = [
    False, False, False, False,
    False, False, True, True, False, False,
    False, False, False, False,
    True
]
SET_MAX = max(SET)
SET_MIN = min(SET)
SET_LENGHT = len(SET)
DIVISOR = 5

# TESTS
def test_main() -> None:
    """
    Main method.
    """

    # Run main
    assert main(set_of_numbers=SET, divisor=DIVISOR) == sum(SUBSETS_DIVISIBLE)
