import math
import statistics
from unittest import TestCase

from src.day7.crabs import (
    calculate_fuel_consumption_for_distance,
    get_least_fuel_for_constant_burn,
    get_least_fuel_for_increasing_burn,
)


class CrabsTest(TestCase):
    def test_the_best_position_for_crabs_to_move_is_the_median_for_constant_fuel(self):
        cases = [
            ([1], 1),
            ([1, 5, 5], 5),
            ([1, 9, 10], 9),
            ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 2),
        ]
        for example_list, expected_answer in cases:
            with self.subTest(msg=f"{example_list}: {expected_answer}"):
                self.assertEqual(expected_answer, statistics.median(example_list))

    def test_can_get_the_amount_of_constant_fuel_required_to_move_all_crabs_to_median(
        self,
    ):
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

    def test_best_position_to_move_to_with_least_movement_is_close_to_the_average(self):
        cases = [
            ([1], 1),
            ([1, 4, 4], 3),
            ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 5),
        ]
        for example_list, expected_answer in cases:
            with self.subTest(msg=f"{example_list}: {expected_answer}"):
                self.assertGreaterEqual(
                    expected_answer, math.floor(statistics.mean(example_list))
                )
                self.assertLessEqual(
                    expected_answer, math.ceil(statistics.mean(example_list))
                )

    def test_get_the_amount_of_increasing_fuel_required_to_move_crabs_to_the_average(
        self,
    ):
        cases = [
            ([1], 0),
            ([1, 4, 4], 5),
            ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 168),
        ]
        for example_list, expected_answer in cases:
            with self.subTest(msg=f"{example_list}: {expected_answer}"):
                self.assertEqual(
                    expected_answer, get_least_fuel_for_increasing_burn(example_list)
                )

    def test_calculates_the_fuel_consumption_for_a_distance(self):
        self.assertEqual(0, calculate_fuel_consumption_for_distance(0, 0))
        self.assertEqual(1, calculate_fuel_consumption_for_distance(0, 1))
        self.assertEqual(3, calculate_fuel_consumption_for_distance(4, 2))
        self.assertEqual(6, calculate_fuel_consumption_for_distance(0, 3))
        self.assertEqual(10, calculate_fuel_consumption_for_distance(4, 8))
        self.assertEqual(15, calculate_fuel_consumption_for_distance(10, 15))
        self.assertEqual(21, calculate_fuel_consumption_for_distance(26, 20))
