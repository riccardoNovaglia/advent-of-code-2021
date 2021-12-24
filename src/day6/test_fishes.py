import time
from unittest import TestCase

from src.day6.fishes import Fishes


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

    # faster tho
    def test_fishes_counter_decreases_every_day_faster(self):
        fishes = Fishes([1])
        fishes.tick_faster()
        self.assertEqual([0], fishes.fishes)

    def test_a_fish_will_spawn_another_when_its_counter_reaches_zero_and_resets_faster(
        self,
    ):
        fishes = Fishes([0])
        fishes.tick_faster()
        self.assertEqual([6, 8], fishes.fishes)
        self.assertEqual(2, fishes.count_fishes())

    def test_a_fish_will_spawn_another_but_more_faster(self):
        fishes = Fishes([0, 1])
        fishes.tick_faster()
        self.assertEqual([0, 6, 8], fishes.fishes)
        fishes.tick_faster()
        self.assertEqual([5, 6, 7, 8], fishes.fishes)


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

    def test_a_quicker_implementation(self):
        iterations = 150

        fishes = Fishes.from_string("3,4,3,1,2")
        t = time.process_time()
        for i in range(iterations):
            fishes.tick_day()
        tick_day_elapsed_time = time.process_time() - t
        print(f"Tick day took {tick_day_elapsed_time}")

        fishes = Fishes.from_string("3,4,3,1,2")
        t = time.process_time()
        for i in range(iterations):
            fishes.tick_faster()
        tick_faster_elapsed_time = time.process_time() - t
        print(f"Tick faster took {tick_faster_elapsed_time}")

        self.assertGreater(abs(tick_day_elapsed_time - tick_faster_elapsed_time), 0.5)
