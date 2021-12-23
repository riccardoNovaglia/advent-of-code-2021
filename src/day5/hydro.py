import itertools

from src.inputs.inputs import get_cleaned_up_input

Point = (int, int)


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.points = (start, end)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def is_horizontal(self):
        return self.start[1] == self.end[1]

    def is_vertical(self):
        return self.start[0] == self.end[0]

    def is_straight(self):
        return self.is_horizontal() or self.is_vertical()

    def ordered_points(self) -> (int, int):
        if self.is_horizontal():
            if self.start[0] > self.end[0]:
                return self.end, self.start
        else:
            if self.start[1] > self.end[1]:
                return self.end, self.start
        return self.start, self.end


class HydroField:
    def __init__(self, x, y):
        self.field = []
        for i in range(y):
            column = [0] * x
            self.field.append(column)

    def mark(self, x, y):
        self.field[y][x] += 1

    def mark_line(self, line: Line):
        start, end = line.ordered_points()
        if line.is_horizontal():
            for i in range(start[0], end[0] + 1):
                self.mark(i, start[1])
        else:
            for i in range(start[1], end[1] + 1):
                self.mark(start[0], i)

    def count_hotspots(self):
        count = 0
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j] > 1:
                    count += 1
        return count


def parse_point(start_string) -> Point:
    [x, y] = start_string.split(",")
    return int(x), int(y)


def parse_line(line) -> Line:
    [start_string, end_string] = line.split(" -> ")
    return Line(parse_point(start_string), parse_point(end_string))


def get_lines_for_input(input_lines: [str]) -> [Line]:
    return [parse_line(line) for line in input_lines]


def get_dimensions(lines: [Line]) -> (int, int):
    flat_points = list(itertools.chain(*[line.points for line in lines]))
    all_x = [point[0] for point in flat_points]
    all_y = [point[1] for point in flat_points]
    return max(all_x) + 1, max(all_y) + 1


def count_hotspots(input_lines: [str]) -> int:
    lines = get_lines_for_input(input_lines)
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
