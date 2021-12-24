import itertools

from src.inputs.inputs import get_raw_input


class Fishes:
    def __init__(self, fishes):
        self.fishes = fishes
        self.fishes.sort()

    def tick_day(self):
        new_generation = []
        for fish in self.fishes:
            if fish > 0:
                new_generation.append(fish - 1)
            else:
                new_generation.append(6)
                new_generation.append(8)
        self.fishes = new_generation

    def tick_faster(self):
        spawners_count = self.fishes.count(0)
        new_gen = [8] * spawners_count
        reset = [6] * spawners_count
        to_age = list(map(lambda fish: fish - 1, self.fishes[spawners_count:]))
        self.fishes = to_age + reset + new_gen
        self.fishes.sort()

    def count_fishes(self) -> int:
        return len(self.fishes)

    @staticmethod
    def from_string(input_string):
        return Fishes([int(fish) for fish in input_string.split(",")])


if __name__ == "__main__":
    input_string = get_raw_input()
    # fishes = Fishes.from_string(input_string)
    # for i in range(80):
    #     fishes.tick_day()
    #     print(f"{i}", end=",")
    # print(f"After 80 days there are now {fishes.count_fishes()} fishes")
    even_more_fishes = Fishes.from_string(input_string)
    for i in range(100):
        even_more_fishes.tick_day()
        print(f"{i}", end=",")
    print(f"After 256 days there are now {even_more_fishes.count_fishes()} fishes")
