import itertools
from dataclasses import dataclass

from src.inputs.inputs import get_cleaned_up_input


@dataclass()
class Point:
    x: int
    y: int

    @staticmethod
    def from_string(string):
        [x, y] = string.split(",")
        return Point(int(x), int(y))


@dataclass()
class Line:
    start: Point
    end: Point

    @staticmethod
    def from_string(string):
        [start_string, end_string] = string.split(" -> ")
        return Line(Point.from_string(start_string), Point.from_string(end_string))

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_straight(self):
        return self.is_horizontal() or self.is_vertical()

    def x_range(self):
        xs = [self.start.x, self.end.x]
        return range(min(xs), max(xs) + 1)

    def y_range(self):
        ys = [self.start.y, self.end.y]
        return range(min(ys), max(ys) + 1)


class HydroField:
    def __init__(self, x, y):
        self.field = [[0] * x for _ in range(y)]

    def mark(self, x, y):
        self.field[y][x] += 1

    def mark_line(self, line: Line):
        if line.is_horizontal():
            for i in line.x_range():
                self.mark(i, line.start.y)
        else:
            for i in line.y_range():
                self.mark(line.start.x, i)

    def count_hotspots(self):
        all_points = list(itertools.chain(*self.field))
        return len(list(filter(lambda point: point > 1, all_points)))


def get_dimensions(lines: [Line]) -> (int, int):
    return (
        max([line.x_range().stop for line in lines]),
        max([line.y_range().stop for line in lines]),
    )


def count_hotspots(input_lines: [str]) -> int:
    lines = [Line.from_string(line) for line in input_lines]

    x, y = get_dimensions(lines)
    field = HydroField(x, y)

    horizontal_lines = list(filter(lambda line: line.is_straight(), lines))

    for line in horizontal_lines:
        field.mark_line(line)
    return field.count_hotspots()


if __name__ == "__main__":
    input_lines = get_cleaned_up_input()
    hotspots = count_hotspots(input_lines)
    print(f"Found {hotspots} hotspots")
