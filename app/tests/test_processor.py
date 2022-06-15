# LIBS
from src.base.processor import Processor

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
def test_constructor():
    """
    Tests the constructor.
    """

    # Initialize the processor
    processor = Processor(set_of_numbers=SET, divisor=DIVISOR)

    # Check the internal variables
    assert processor.set_of_numbers == SET
    assert processor.divisor == DIVISOR


def test_update_set_of_numbers():
    """
    Tests the update_set_of_numbers method.
    """

    # Initialize the processor
    processor = Processor()

    # Define the set of numbers
    processor.update_set_of_numbers(SET)

    # Check the internal variables
    assert processor.set_of_numbers == SET
    assert processor.set_ordered == SET_ORDERED
    assert processor.set_max_number == SET_MAX
    assert processor.set_min_number == SET_MIN
    assert processor.set_length == SET_LENGHT


def test_update_divisor():
    """
    Tests the update_divisor method.
    """

    # Initialize the processor
    processor = Processor()

    # Update the divisor
    processor.update_divisor(DIVISOR)

    # Check the internal variables
    assert processor.divisor == DIVISOR


def test_yield_subset():
    """
    Tests the yield_subset method.
    """

    # Initialize the processor
    processor = Processor(set_of_numbers=SET)

    # Count subsets
    counter = [0] * len(SUBSETS_LIST)

    for subset in processor.yield_subset():

        # Get the index of the subset
        try:
            index = SUBSETS_LIST.index(subset)
        except ValueError:
            print(f"Subset {subset} not found in the subset list.")
            raise ValueError(f"Subset {subset} not found in the subset list.")

        # Increment the counter
        counter[index] += 1

    # Check the counter
    assert counter == [1] * len(SUBSETS_LIST)


def test_is_subset_divisible():
    """
    Tests the is_subset_divisible method.
    """

    # Initialize the processor
    processor = Processor(set_of_numbers=SET)

    # Check the subset divisible
    for i, subset in enumerate(SUBSETS_LIST):
        assert processor.is_subset_divisible(subset) is SUBSETS_DIVISIBLE[i]


def test_count_divisible_subsets():
    """
    Tests the count_divisible_subsets method.
    """

    # Initialize the processor
    processor = Processor(set_of_numbers=SET)

    # Check the number of divisible subsets
    assert processor.count_divisible_subsets() == sum(SUBSETS_DIVISIBLE)


def test_get_count_of_all_non_empty_subsets():
    """
    Tests the get_count_of_all_non_empty_subsets method.
    """

    # Initialize the processor
    processor = Processor(set_of_numbers=SET)

    # Check the number of non empty subsets
    assert processor.get_count_of_all_non_empty_subsets() == len(SUBSETS_LIST)
