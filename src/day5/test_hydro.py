from typing import Type
from unittest import TestCase

from src.day5.hydro import HydroField, Line, Point, count_hotspots, get_dimensions

p: Type[Point] = Point
l: Type[Line] = Line


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
        field.mark_line(l(p(0, 0), p(1, 0)))
        self.assertEqual([[1, 1], [0, 0]], field.field)

    def test_increases_the_value_for_a_vertical_line(self):
        field = HydroField(2, 2)
        field.mark_line(l(p(1, 0), p(1, 1)))
        self.assertEqual([[0, 1], [0, 1]], field.field)

    def test_increases_a_horizontal_line_expressed_backwards(self):
        field = HydroField(2, 2)
        field.mark_line(l(p(1, 0), p(0, 0)))
        self.assertEqual([[1, 1], [0, 0]], field.field)

    def test_increases_a_diagonal_line(self):
        field = HydroField(2, 2)
        field.mark_line(l(p(0, 0), p(1, 1)))
        self.assertEqual([[1, 0], [0, 1]], field.field)

    def test_increases_a_diagonal_line_backwards(self):
        field = HydroField(2, 2)
        field.mark_line(l(p(1, 0), p(0, 1)))
        self.assertEqual([[0, 1], [1, 0]], field.field)

    def test_counts_hotspots(self):
        field = HydroField(2, 2)
        field.mark(0, 0)
        field.mark(0, 0)
        self.assertEqual(1, field.count_hotspots())
        field.mark(1, 0)
        field.mark(1, 0)
        self.assertEqual(2, field.count_hotspots())


class TestLine(TestCase):
    def test_line_can_tell_its_direction(self):
        self.assertEqual("horizontal", l(p(0, 0), p(5, 0)).direction)
        self.assertEqual("vertical", l(p(0, 3), p(0, 4)).direction)

    def test_line_can_tell_if_its_straight(self):
        self.assertTrue(l(p(0, 3), p(0, 4)).is_straight())
        self.assertFalse(l(p(1, 3), p(2, 4)).is_straight())

    def test_can_be_created_from_a_string(self):
        line = Line.from_string("0,0 -> 0,1")
        self.assertEqual(l(p(0, 0), p(0, 1)), line)

    def test_returns_its_max_x_y(self):
        self.assertEqual(2, l(p(2, 3), p(1, 4)).max_x())
        self.assertEqual(4, l(p(0, 3), p(0, 4)).max_y())

    def test_returns_its_x_range_and_y_range_with_inclusive_ends_and_right_step(self):
        self.assertEqual(range(1, 3), l(p(1, 0), p(2, 0)).x_range())
        self.assertEqual(range(2, 0, -1), l(p(2, 0), p(1, 0)).x_range())

        self.assertEqual(range(3, 6), l(p(2, 3), p(2, 5)).y_range())
        self.assertEqual(range(5, 2, -1), l(p(0, 5), p(0, 3)).y_range())


class TestPoint(TestCase):
    def test_point_can_be_created_from_a_string(self):
        self.assertEqual(Point(2, 3), Point.from_string("2,3"))


class TestWithInput(TestCase):
    def test_finds_the_max_x_y_for_a_list_of_lines(self):
        max_x, max_y = get_dimensions(
            [
                l(p(0, 0), p(0, 1)),
                l(p(3, 2), p(5, 2)),
                l(p(0, 4), p(0, 1)),
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
