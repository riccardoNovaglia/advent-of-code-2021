from unittest import TestCase

from src.day1.increments import count_increments, count_windows_increments, get_windows


class IncrementsTest(TestCase):
    def test_counts_lines_with_number_increments(self):
        cases = [
            ([1], 0),
            ([1, 2], 1),
            ([1, 2, 2], 1),
            ([1, 2, 1], 1),
            ([1, 2, 2, 3], 2),
            ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
        ]
        for input_strings, expected_increments in cases:
            with self.subTest(msg=f"{input_strings}: {expected_increments}"):
                self.assertEqual(count_increments(input_strings), expected_increments)


class Windows(TestCase):
    def test_creates_windows_out_of_the_list_of_given_measurements(self):
        cases = [
            ([1], []),
            ([1, 2], []),
            ([1, 2, 3], [(1, 2, 3)]),
            ([1, 2, 3, 4], [(1, 2, 3), (2, 3, 4)]),
            (
                [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],
                [
                    (199, 200, 208),
                    (200, 208, 210),
                    (208, 210, 200),
                    (210, 200, 207),
                    (200, 207, 240),
                    (207, 240, 269),
                    (240, 269, 260),
                    (269, 260, 263),
                ],
            ),
        ]
        for input_strings, windows in cases:
            with self.subTest(msg=f"{input_strings}: {windows}"):
                self.assertEqual(get_windows(input_strings), windows)

    def test_counts_windows_increments(self):
        cases = [
            ([1, 2, 3], 0),
            ([1, 1, 1, 2, 3], 2),
            ([1, 1, 1, 2, 3, 4], 3),
            ([1, 1, 1, 2, 1, 1], 1),
            ([1, 1, 1, 2, 1, 2], 2),
            ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5),
        ]
        for windows, expected_increments in cases:
            with self.subTest(msg=f"{windows}: {expected_increments}"):
                self.assertEqual(count_windows_increments(windows), expected_increments)
