from typing import List


def validate_inputs(arr: List[str]) -> None:
    """Checks the input grid for symmetry, ascii characters and elements only as "0" and "1".
       This function loops through the input grid, for each row and performs the following checks.

    :param List[str] arr: A list of strings to be validated i.e. input grid
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
