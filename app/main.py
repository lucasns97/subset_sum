# LIBS
from src.base.processor import Processor
from src.environment import DEFAULT_DIVISOR, DEFAULT_SET
from typing import Set

# METHODS

# MAIN
def main(set_of_numbers: Set[int] = DEFAULT_SET, divisor: int = DEFAULT_DIVISOR) -> int:
    """
    Main method.

    :param set_of_numbers: Set of numbers to be used in the search.
    :param divisor: Divisor to be used in the search.
    :return: Number of subsets divisible by the divisor.
    """

    # Initialize the processor
    processor = Processor(set_of_numbers=set_of_numbers, divisor=divisor)

    # Calculate the subset count that are divisible by the divisor
    subset_count = processor.count_divisible_subsets()

    # Print the subset count
    print(f">> There are {subset_count} subsets divisible by {divisor}.")

    return subset_count

# RUN
if __name__ == '__main__':
    
    print()

    # Retrieve user input
    try:
        first_number_of_set = int(input('>> Enter the lowest number of the set: '))
        last_number_of_set = int(input('>> Enter the highest number of the set: '))
        divisor = int(input('>> Enter the divisor (!= 0): '))
        assert divisor != 0, 'The divisor cannot be 0.'

        print()

    # Handle the error
    except ValueError:
        print('Invalid input.\n')
        exit()

    # Build set
    set_of_numbers = {i for i in range(first_number_of_set, last_number_of_set + 1)}
    
    # Run main
    _ = main(set_of_numbers=set_of_numbers, divisor=divisor)
    print()