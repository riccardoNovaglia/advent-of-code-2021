import statistics
from unittest import TestCase

from src.day7.crabs import get_least_fuel_for_constant_burn


class CrabsTest(TestCase):
    def test_the_best_position_for_crabs_to_move_is_the_median(self):
        cases = [
            ([1], 1),
            ([1, 5, 5], 5),
            ([1, 9, 10], 9),
            ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 2),
        ]
        for example_list, expected_answer in cases:
            with self.subTest(msg=f"{example_list}: {expected_answer}"):
                self.assertEqual(expected_answer, statistics.median(example_list))

    def test_can_get_the_amount_of_fuel_required_to_move_all_crabs_to_the_median(self):
        cases = [
            ([1], 0),
            ([1, 5, 5], 4),
            ([1, 9, 10], 9),
            ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 37),
        ]
        for example_list, expected_answer in cases:
            with self.subTest(msg=f"{example_list}: {expected_answer}"):
                self.assertEqual(
                    expected_answer, get_least_fuel_for_constant_burn(example_list)
                )
