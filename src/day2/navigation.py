class JumpedOutOfWaterException(Exception):
    pass


movements = {
    "forward": lambda position, amount: (position[0] + amount, position[1]),
    "down": lambda position, amount: (position[0], position[1] + amount),
    "up": lambda position, amount: (position[0], position[1] - amount),
}


def navigate(directions) -> (int, int):
    position = (0, 0)
    for [direction, amount] in [direction.split(" ") for direction in directions]:
        position = movements[direction](position, int(amount))
        if position[1] < 0:
            raise JumpedOutOfWaterException()

    return position


movements_with_aim = {
    "forward": lambda position, aim, amount: (
        (position[0] + amount, position[1] + (amount * aim)),
        aim,
    ),
    "down": lambda position, aim, amount: (position, aim + amount),
    "up": lambda position, aim, amount: (position, aim - amount),
}


def navigate_with_aim(directions: [str]) -> (int, int):
    position = 0, 0
    aim = 0
    for [direction, amount] in [direction.split(" ") for direction in directions]:
        position, aim = movements_with_aim[direction](position, aim, int(amount))
        if position[1] < 0:
            raise JumpedOutOfWaterException()

    return position


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        directions = file.readlines()
        horizontal, depth = navigate(directions)
        print(f"End state is {horizontal},-{depth}, multiplied: {horizontal * depth}")
        horizontal, depth = navigate_with_aim(directions)
        print(
            f"End state with aim is {horizontal},-{depth}, multiplied:"
            f" {horizontal * depth}"
        )
