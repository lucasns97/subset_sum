# LIBS
from typing import Set, Generator
from tqdm import tqdm

# CONSTANTS
from src.environment import DEFAULT_DIVISOR, DEFAULT_SET, DEBUG


# CLASS
class Processor:

    def __init__(self, set_of_numbers: Set[int] = DEFAULT_SET, divisor: int = DEFAULT_DIVISOR) -> None:

        # Internal variables
        self.update_set_of_numbers(set_of_numbers)
        self.update_divisor(divisor)

    def update_set_of_numbers(self, set_of_numbers: Set[int]) -> None:
        """
        Updates the set of numbers to be used in the search.

        :param set_of_numbers: Set of numbers to be used in the search.
        :return: None
        """
        self.set_of_numbers = set_of_numbers
        self.set_ordered = sorted(list(self.set_of_numbers))
        self.set_max_number = max(self.set_of_numbers)
        self.set_min_number = min(self.set_of_numbers)
        self.set_length = len(self.set_of_numbers)

    def update_divisor(self, divisor: int) -> None:
        """
        Updates the divisor to be used in the search.

        :param divisor: Divisor to be used in the search.
        :return: None
        """
        self.divisor = divisor

    def yield_subset(self) -> Generator:
        """
        Yields a subset from the set of numbers.

        :return: Subset of the set of numbers.
        """

        # Define the masks
        masks = [1 << i for i in range(self.set_length)]

        # Iterate over the each possible subset
        for i in range(1 << self.set_length):

            # Get the subset
            subset = {ss for mask, ss in zip(masks, self.set_of_numbers) if i & mask}

            # Skip the empty subset
            if not subset:
                continue

            # Yield the subset
            yield subset

    def get_count_of_all_non_empty_subsets(self) -> int:
        """
        Counts the number of all subsets.

        :return: Number of all subsets.
        """

        return (1 << self.set_length) - 1

    def is_subset_divisible(self, subset: Set[int]) -> bool:
        """
        Checks if the sum of the numbers within a subset is divisible by the divisor.

        :param subset: Subset to be checked.
        :return: True if the sum of subset numbers is divisible by the divisor.
        """

        # Check if the subset is divisible by the divisor
        return sum(subset) % self.divisor == 0

    def count_divisible_subsets(self) -> int:
        """
        Counts the number of subsets that are divisible by the divisor.

        :return: Number of divisible subsets.
        """

        if DEBUG:
            print(f"[DEBUG] Counting the number of subsets that are divisible by {self.divisor}.")
            print(f"[DEBUG] The set of numbers is {self.set_of_numbers}.")

        # Count the number of divisible subsets
        sum_of = 0

        # Iterate over the subsets
        pbar = tqdm(
            self.yield_subset(),
            desc="[DEBUG] Counting divisible subsets",
            disable=not DEBUG,
            total=self.get_count_of_all_non_empty_subsets()
        )

        for subset in pbar:

            # Check if the subset is divisible by the divisor
            if self.is_subset_divisible(subset):
                sum_of += 1

            # Update the progress bar
            if DEBUG:
                pbar.set_postfix({"Divisible subsets": sum_of})

        return sum_of
