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

    def count_fishes(self) -> int:
        return len(self.fishes)

    @staticmethod
    def from_string(input_string):
        return Fishes([int(fish) for fish in input_string.split(",")])


class FishesGroup:
    age_groups = range(9)

    def __init__(self, fishes):
        self.groups = {age: fishes.count(age) for age in self.age_groups}

    def tick_day(self):
        spawn_generation = self.groups[0]
        for age_group in self.age_groups:
            if age_group == 8:
                self.groups[age_group] = spawn_generation
            elif age_group == 6:
                self.groups[age_group] = self.groups[age_group + 1] + spawn_generation
            else:
                self.groups[age_group] = self.groups[age_group + 1]

    def count_fishes(self) -> int:
        return sum([count for age, count in self.groups.items()])

    @staticmethod
    def from_string(input_string):
        return FishesGroup([int(fish) for fish in input_string.split(",")])


if __name__ == "__main__":
    input_string = get_raw_input()
    fishes = Fishes.from_string(input_string)
    for i in range(80):
        fishes.tick_day()
    print(f"After 80 days there are now {fishes.count_fishes()} fishes")
    fishes_group = FishesGroup.from_string(input_string)
    for i in range(80):
        fishes_group.tick_day()
    print(
        f"After 80 days there are now {fishes_group.count_fishes()} fishes - using "
        f"groups"
    )
    final_fishes_group = FishesGroup.from_string(input_string)
    for i in range(256):
        final_fishes_group.tick_day()
    print(f"After 256 days there are now {final_fishes_group.count_fishes()} fishes")
