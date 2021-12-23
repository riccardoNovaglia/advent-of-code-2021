from src.inputs.inputs import get_cleaned_up_input


def diagnose(readings: [str]) -> (str, str):
    readings_length = len(readings[0].strip())

    gamma = ""
    for i in range(readings_length):
        stream = [reading[i] for reading in readings]
        if stream.count("0") > len(stream) / 2:
            gamma += "0"
        elif stream.count("0") == len(stream) / 2:
            gamma += "1"
        else:
            gamma += "1"

    epsilon = "".join(["0" if digit == "1" else "1" for digit in gamma])
    return gamma, epsilon


def oxygen_and_co2_ratings(readings: [str]) -> (str, str):
    oxygen_candidates = readings.copy()
    bit_index = 0
    while len(set(oxygen_candidates)) != 1:
        gamma, _ = diagnose(oxygen_candidates)
        popular = gamma[bit_index]
        oxygen_candidates = list(
            filter(lambda reading: reading[bit_index] == popular, oxygen_candidates)
        )
        bit_index += 1

    co2_candidates = readings.copy()
    bit_index = 0
    while len(set(co2_candidates)) != 1:
        _, epsilon = diagnose(co2_candidates)
        least_popular = epsilon[bit_index]
        co2_candidates = list(
            filter(lambda reading: reading[bit_index] == least_popular, co2_candidates)
        )
        bit_index += 1
        _, epsilon = diagnose(co2_candidates)

    return oxygen_candidates[0], co2_candidates[0]


if __name__ == "__main__":
    readings = get_cleaned_up_input()
    gamma, epsilon = diagnose(readings)
    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)
    print(f"Gamma: {gamma} ({gamma_decimal}), Epsilon: {epsilon} ({epsilon_decimal})")
    print(f"Power consumption: {gamma_decimal * epsilon_decimal}")
    oxygen, co2 = oxygen_and_co2_ratings(readings)
    oxygen_decimal = int(oxygen, 2)
    co2_decimal = int(co2, 2)
    print(f"Oxygen: {oxygen} ({oxygen_decimal}), CO2: {co2} ({co2_decimal})")
    print(f"Life support rating: {oxygen_decimal * co2_decimal}")
