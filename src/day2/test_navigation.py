from unittest import TestCase

from src.day2.navigation import JumpedOutOfWaterException, navigate, navigate_with_aim


class Test(TestCase):
    def test_navigates_and_returns_the_end_coordinates(self):
        cases = [
            ([], (0, 0)),
            (["down 1"], (0, 1)),
            (["forward 1"], (1, 0)),
            (["down 1", "up 1"], (0, 0)),
            (["down 1", "down 1", "forward 1"], (1, 2)),
            (
                ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"],
                (15, 10),
            ),
        ]
        for directions, end_position in cases:
            with self.subTest(msg=f"{directions}: {end_position}"):
                self.assertEqual(navigate(directions), end_position)

    def test_uses_aim_to_calculate_the_end_coordinates(self):
        cases = [
            ([], (0, 0)),
            (["forward 1"], (1, 0)),
            (["down 1"], (0, 0)),
            (["down 1", "forward 1"], (1, 1)),
            (["down 2", "forward 1"], (1, 2)),
            (["down 2", "forward 2"], (2, 4)),
            (["down 2", "forward 1", "up 1", "forward 1"], (2, 3)),
            (
                ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"],
                (15, 60),
            ),
        ]
        for directions, end_position in cases:
            with self.subTest(msg=f"{directions}: {end_position}"):
                self.assertEqual(navigate_with_aim(directions), end_position)

    def test_throws_an_error_if_we_jump_out_of_the_water(self):
        with self.assertRaises(JumpedOutOfWaterException):
            navigate(["up 1"])
