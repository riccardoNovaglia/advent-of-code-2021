from unittest import TestCase

from src.day5.hydro import HydroField, Line, count_hotspots, get_dimensions


class TestHydroField(TestCase):
    def test_creates_an_empty_field_with_given_dimensions(self):
        field = HydroField(2, 2)
        self.assertEqual([[0, 0], [0, 0]], field.field)

    def test_increases_the_value_of_a_set_of_coordinates(self):
        field = HydroField(2, 2)
        field.mark(0, 0)
        field.mark(1, 1)
        self.assertEqual([[1, 0], [0, 1]], field.field)

    def test_increases_the_value_for_a_horizontal_line(self):
        field = HydroField(2, 2)
        field.mark_line(Line((0, 0), (1, 0)))
        self.assertEqual([[1, 1], [0, 0]], field.field)

    def test_increases_the_value_for_a_vertical_line(self):
        field = HydroField(2, 2)
        field.mark_line(Line((1, 0), (1, 1)))
        self.assertEqual([[0, 1], [0, 1]], field.field)

    def test_increases_a_horizontal_line_expressed_backwards(self):
        field = HydroField(2, 2)
        field.mark_line(Line((1, 0), (0, 0)))
        self.assertEqual([[1, 1], [0, 0]], field.field)

    def test_counts_hotspots(self):
        field = HydroField(2, 2)
        field.mark(0, 0)
        field.mark(0, 0)
        self.assertEqual(1, field.count_hotspots())
        field.mark(1, 0)
        field.mark(1, 0)
        self.assertEqual(2, field.count_hotspots())


class TestLine(TestCase):
    def test_line_can_tell_if_its_horizontal(self):
        self.assertTrue(Line((0, 0), (5, 0)).is_horizontal())
        self.assertFalse(Line((0, 3), (0, 4)).is_horizontal())

    def test_line_can_tell_if_its_vertical(self):
        self.assertTrue(Line((0, 3), (0, 4)).is_vertical())
        self.assertFalse(Line((0, 0), (5, 0)).is_vertical())

    def test_line_can_tell_if_its_straight(self):
        self.assertTrue(Line((0, 3), (0, 4)).is_straight())
        self.assertFalse(Line((1, 3), (2, 4)).is_straight())

    def test_can_return_its_points_in_increasing_order(self):
        self.assertEqual(((0, 0), (0, 1)), Line((0, 0), (0, 1)).ordered_points())
        self.assertEqual(((0, 0), (0, 1)), Line((0, 1), (0, 0)).ordered_points())
        self.assertEqual(((0, 0), (1, 0)), Line((1, 0), (0, 0)).ordered_points())

    def test_can_be_created_from_a_string(self):
        line = Line.from_string("0,0 -> 0,1")
        self.assertEqual(Line((0, 0), (0, 1)), line)

    def test_returns_its_maximum_x_and_y(self):
        self.assertEqual((0, 4), Line((0, 3), (0, 4)).max_dimensions())
        self.assertEqual((2, 4), Line((1, 3), (2, 4)).max_dimensions())


class TestWithInput(TestCase):
    def test_finds_the_max_x_y_for_a_list_of_lines(self):
        max_x, max_y = get_dimensions(
            [
                Line((0, 0), (0, 1)),
                Line((3, 2), (5, 2)),
                Line((0, 4), (0, 1)),
            ]
        )
        self.assertEqual((6, 5), (max_x, max_y))

    def test_gives_the_right_answer_to_the_sample_provided(self):
        hotspots = count_hotspots(
            [
                "0,9 -> 5,9",
                "8,0 -> 0,8",
                "9,4 -> 3,4",
                "2,2 -> 2,1",
                "7,0 -> 7,4",
                "6,4 -> 2,0",
                "0,9 -> 2,9",
                "3,4 -> 1,4",
                "0,0 -> 8,8",
                "5,5 -> 8,2",
            ]
        )
        self.assertEqual(5, hotspots)
