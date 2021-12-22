def get_increments(input_lines):
    readings = [int(line.strip()) for line in input_lines if line != ""]

    increments_count = 0
    for index in range(len(readings) - 1):
        if readings[index] < readings[index + 1]:
            increments_count += 1

    return increments_count


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        print(get_increments(file.readlines()))
