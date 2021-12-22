from unittest import TestCase

from src.day1.increments import get_increments


class IncrementsTest(TestCase):
    def test_counts_lines_with_number_increments(self):
        cases = [
            (["1"], 0),
            (["1", "2"], 1),
            (["1", "2", "2"], 1),
            (["1", "2", "1"], 1),
            (["1", "2", "2", "3"], 2),
            (["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"], 7),
        ]
        for input_string, expected_increments in cases:
            with self.subTest(msg=f"{input_string}: {expected_increments}"):
                self.assertEqual(get_increments(input_string), expected_increments)
