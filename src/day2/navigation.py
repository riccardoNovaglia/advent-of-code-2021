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


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        directions = file.readlines()
        horizontal, depth = navigate(directions)
        print(f"End state is {horizontal},-{depth}, multiplied: {horizontal * depth}")
