from unittest import TestCase

from src.day3.diagnostic import diagnose, oxygen_and_co2_ratings


class Test(TestCase):
    def test_diagnose(self):
        cases = [
            (["0"], ("0", "1")),
            (["0", "1", "1"], ("1", "0")),
            (["00"], ("00", "11")),
            (["10", "01", "10"], ("10", "01")),
            (
                [
                    "00100",
                    "11110",
                    "10110",
                    "10111",
                    "10101",
                    "01111",
                    "00111",
                    "11100",
                    "10000",
                    "11001",
                    "00010",
                    "01010",
                ],
                ("10110", "01001"),
            ),
        ]
        for readings, gamma_epsilon in cases:
            with self.subTest(msg=f"{readings}: {gamma_epsilon}"):
                self.assertEqual(diagnose(readings), gamma_epsilon)

    def test_does_something_interesting_if_theres_an_even_number_of_readings(self):
        cases = [
            (["0", "0"], ("0", "1")),
            (["11", "11"], ("11", "00")),
        ]
        for readings, gamma_epsilon in cases:
            with self.subTest(msg=f"{readings}: {gamma_epsilon}"):
                self.assertEqual(diagnose(readings), gamma_epsilon)

    def test_oxygen_and_co2_ratings(self):
        cases = [
            (["0", "1", "1"], ("1", "0")),
            (["10", "01", "10"], ("10", "01")),
            (["10", "01", "11"], ("11", "01")),
            (
                [
                    "00100",
                    "11110",
                    "10110",
                    "10111",
                    "10101",
                    "01111",
                    "00111",
                    "11100",
                    "10000",
                    "11001",
                    "00010",
                    "01010",
                ],
                ("10111", "01010"),
            ),
        ]
        for readings, gamma_epsilon in cases:
            with self.subTest(msg=f"{readings}: {gamma_epsilon}"):
                self.assertEqual(oxygen_and_co2_ratings(readings), gamma_epsilon)
