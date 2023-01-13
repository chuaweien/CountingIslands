import unittest
from run import IslandsCounting


class TestingStringMethods(unittest.TestCase):

    def test_empty_input(self):
        counts = IslandsCounting()
        self.assertRaises(ValueError, counts.count_islands,
                          "data/test_data/island_empty.txt")

    def test_input_validation(self):
        counts = IslandsCounting()
        self.assertRaises(AssertionError, counts.count_islands,
                          "data/test_data/islands_input_error.txt")

    def test_algo(self):
        counts = IslandsCounting()
        self.assertEqual(counts.count_islands(
            "data/test_data/islands.txt"), 4)


if __name__ == "__main__":
    unittest.main()
