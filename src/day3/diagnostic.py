def diagnose(readings: [str]) -> (str, str):
    readings_length = len(readings[0].strip())

    gamma = ""
    for i in range(readings_length):
        stream = [reading[i] for reading in readings]
        if stream.count("0") > len(stream) / 2:
            gamma += "0"
        else:
            gamma += "1"

    epsilon = "".join(["0" if digit == "1" else "1" for digit in gamma])
    return gamma, epsilon


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        gamma, epsilon = diagnose(file.readlines())
        gamma_decimal = int(gamma, 2)
        epsilon_decimal = int(epsilon, 2)
        print(
            f"Gamma: {gamma} ({gamma_decimal}), Epsilon: {epsilon} ({epsilon_decimal})"
        )
        print(f"Power consumption: {gamma_decimal * epsilon_decimal}")
