import math
import statistics

from src.inputs.inputs import get_raw_input


def get_least_fuel_for_constant_burn(crabs_list):
    best_position = statistics.median(crabs_list)
    return sum([abs(crab_position - best_position) for crab_position in crabs_list])


def calculate_fuel_consumption_for_distance(start, end):
    previous = 0
    distance = abs(start - end)
    return sum([i + previous for i in range(1, distance + 1)])


def get_least_fuel_for_increasing_burn(crabs_list):
    mean = statistics.mean(crabs_list)
    floored_mean = math.floor(mean)
    ceil_mean = math.ceil(mean)

    floor_mean_consumption = [
        calculate_fuel_consumption_for_distance(crab_position, floored_mean)
        for crab_position in crabs_list
    ]
    ceil_mean_consumption = [
        calculate_fuel_consumption_for_distance(crab_position, ceil_mean)
        for crab_position in crabs_list
    ]

    return min([sum(floor_mean_consumption), sum(ceil_mean_consumption)])


if __name__ == "__main__":
    input_strings = get_raw_input()
    crabs_positions = [int(x) for x in input_strings.split(",")]
    print(
        f"Fuel consumed to move to optimal position with constant fuel consumption is "
        f"{get_least_fuel_for_constant_burn(crabs_positions)}"
    )
    print(
        f"Fuel consumed to move to optimal position with increasing fuel consumption "
        f"is {get_least_fuel_for_increasing_burn(crabs_positions)}"
    )
