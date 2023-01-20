import unittest
from src.run import IslandsCounting


islands = IslandsCounting()


class TestCases(unittest.TestCase):

    # input is empty, should raise error
    def test_empty_input(self):
        grid = []
        self.assertRaises(ValueError, islands.count_islands,
                          grid)

    # input shape is asymmetrical, should raise error
    def test_input_validation(self):
        grid = ['100000001',
                '010000000',
                '111000100',
                '110001110',
                '001100110',
                '00100001',  # missing 1 element
                '110000011',
                '001111100']
        self.assertRaises(AssertionError, islands.count_islands,
                          grid)

    # test the algo is correct, output should be 4
    def test_algo(self):
        grid = ['000000000',
                '010000000',
                '111000100',
                '110001110',
                '000001100',
                '001000000',
                '110000000',
                '000001100']
        self.assertEqual(islands.count_islands(
            grid), 4)

    def test_edge_cases(self):
        # Single island: The grid contains a single island made up of a single 1.
        grid = ['1']
        self.assertEqual(islands.count_islands(
            grid), 1)

        # No islands: The grid contains only 0's.
        grid = ['000000000']
        self.assertEqual(islands.count_islands(
            grid), 0)

        # Many islands: The grid is very large, with a large number of 1's and 0's
        grid = islands.read_input_file("data/test_data/islands_large.txt")
        self.assertEqual(islands.count_islands(
            grid), 2594)

        # Sparse islands: The grid is very sparse, with a small number of 1's and a
        # large number of 0's.
        grid = islands.read_input_file(
            "data/test_data/islands_large_sparse.txt")
        self.assertEqual(islands.count_islands(
            grid), 3)

        # Island with a hole: The grid contains an island where some cells inside the island are 0.
        grid = ['000110000',
                '001001000',
                '111000100',
                '001001110',
                '000101100',
                '000000000',
                '000000000',
                '000000000']
        self.assertEqual(islands.count_islands(
            grid), 1)

        # Island with a bridge: The grid contains an island where the cells are not all connected
        # but there is a bridge that connects cells that are not next to each other.
        grid = ['000110000',
                '001001000',
                '111000100',
                '001111110',
                '000100000',
                '000010000',
                '000101000',
                '000010000']
        self.assertEqual(islands.count_islands(
            grid), 1)


if __name__ == "__main__":
    unittest.main()
