from typing import List


def validate_inputs(arr: List) -> None:
    """Ensure that each row in array has same number of elements.
    If array is asymmetrical, it will output an error with row index.

    :param List arr: input 2D array
    :return None: None
    """
    n_elements = len(arr[0])

    for x, row in enumerate(arr):
        # validate each row has same number of elements
        assert len(row) == n_elements, "Row {} is not symmetrical!".format(x)

        # validate each element are ascii
        assert all(ord(
            element) < 128 for element in row), "Row {} contains non-ascii characters".format(x)

        # validate each element are either "0" or "1"
        assert all([element in ["0", "1"] for element in row]
                   ), "Row {} contains elements other than '0' or '1'".format(x)
