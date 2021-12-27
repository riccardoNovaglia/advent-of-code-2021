from unittest import TestCase

from src.day6.fishes import Fishes, FishesGroup


class TestFishes(TestCase):
    def test_creates_fishes_with_the_given_input(self):
        fishes = Fishes([1])
        self.assertEqual([1], fishes.fishes)
        self.assertEqual(1, fishes.count_fishes())

    def test_fishes_counter_decreases_every_day(self):
        fishes = Fishes([1])
        fishes.tick_day()
        self.assertEqual([0], fishes.fishes)

    def test_a_fish_will_spawn_another_when_its_counter_reaches_zero_and_resets(self):
        fishes = Fishes([0])
        fishes.tick_day()
        self.assertEqual([6, 8], fishes.fishes)
        self.assertEqual(2, fishes.count_fishes())

    def test_a_fish_will_spawn_another_but_more(self):
        fishes = Fishes([0, 1])
        fishes.tick_day()
        self.assertEqual([6, 8, 0], fishes.fishes)
        fishes.tick_day()
        self.assertEqual([5, 7, 6, 8], fishes.fishes)


class TestFishesGroups(TestCase):
    def test_creates_fishes_and_groups_them_by_age(self):
        fishes = FishesGroup([1, 4, 6, 6, 8, 8, 8])
        self.assertEqual(
            {
                0: 0,
                1: 1,
                2: 0,
                3: 0,
                4: 1,
                5: 0,
                6: 2,
                7: 0,
                8: 3,
            },
            fishes.groups,
        )
        self.assertEqual(7, fishes.count_fishes())

    def test_ages_shift_left_daily(self):
        fishes = FishesGroup([1, 4, 6, 6, 8, 8, 8])
        fishes.tick_day()
        self.assertEqual(
            {
                0: 1,
                1: 0,
                2: 0,
                3: 1,
                4: 0,
                5: 2,
                6: 0,
                7: 3,
                8: 0,
            },
            fishes.groups,
        )

    def test_age_0_groups_reset_to_6_and_generates_a_new_gen_at_8(self):
        fishes = FishesGroup([0, 0, 0, 7])
        fishes.tick_day()
        self.assertEqual(
            {
                0: 0,
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 4,
                7: 0,
                8: 3,
            },
            fishes.groups,
        )


class TestInput(TestCase):
    def test_fishes_can_be_created_from_input_string(self):
        fishes = Fishes.from_string("1,2,3")
        self.assertEqual([1, 2, 3], fishes.fishes)

    def test_works_with_the_sample_input(self):
        fishes = Fishes.from_string("3,4,3,1,2")
        fishes.tick_day()
        expected = [2, 3, 2, 0, 1]
        expected.sort()
        self.assertEqual(expected, fishes.fishes)
        for i in range(17):
            fishes.tick_day()
        expected_fishes = [
            6,
            0,
            6,
            4,
            5,
            6,
            0,
            1,
            1,
            2,
            6,
            0,
            1,
            1,
            1,
            2,
            2,
            3,
            3,
            4,
            6,
            7,
            8,
            8,
            8,
            8,
        ]
        expected_fishes.sort()
        actual_fishes = fishes.fishes
        actual_fishes.sort()
        self.assertEqual(
            expected_fishes,
            actual_fishes,
        )
        self.assertEqual(26, fishes.count_fishes())

    def test_groups_work_with_the_sample_input(self):
        fishes = FishesGroup.from_string("3,4,3,1,2")
        for i in range(18):
            fishes.tick_day()
        self.assertEqual(26, fishes.count_fishes())
