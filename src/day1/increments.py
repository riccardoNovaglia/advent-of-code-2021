def get_windows(input_readings: [int]) -> [(int, int, int)]:
    windows = []
    for index in range(len(input_readings) - 2):
        windows.append(
            (
                input_readings[index],
                input_readings[index + 1],
                input_readings[index + 2],
            )
        )
    return windows


def count_increments(readings: [int]) -> int:
    increments_count = 0
    for index in range(len(readings) - 1):
        if readings[index] < readings[index + 1]:
            increments_count += 1
    return increments_count


def count_windows_increments(readings: [int]) -> int:
    windows = get_windows(readings)
    window_sums = [x + y + z for (x, y, z) in windows]
    return count_increments(window_sums)


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        readings = [int(line.strip()) for line in (file.readlines()) if line != ""]
        print("readings increments: ", count_increments(readings))
        print("windowed increments: ", count_windows_increments(readings))
