import statistics

from src.inputs.inputs import get_raw_input


def get_least_fuel_for_constant_burn(crabs_list):
    best_position = statistics.median(crabs_list)
    return sum([abs(crab_position - best_position) for crab_position in crabs_list])


if __name__ == "__main__":
    input_strings = get_raw_input()
    crabs_positions = [int(x) for x in input_strings.split(",")]
    print(
        f"Median position of the given crabs is "
        f"{get_least_fuel_for_constant_burn(crabs_positions)}"
    )
