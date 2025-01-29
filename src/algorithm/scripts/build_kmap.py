def get_coordinate(row: list, coord_component: str) -> int:
    if coord_component == "x":
        first_index = 0
        second_index = 1
    elif coord_component == "y":
        first_index = 2
        second_index = 3
    else:
        raise Exception("Invalid coordinate component")

    if row[first_index] == 0 and row[second_index] == 0:
        return 0
    elif row[first_index] == 0 and row[second_index] == 1:
        return 1
    elif row[first_index] == 1 and row[second_index] == 1:
        return 2
    elif row[first_index] == 1 and row[second_index] == 0:
        return 3
    else:
        raise Exception("Invalid row values")


def build_map(truth_table: list) -> list:
    """_summary_
        K-MAP Navigation:
        AB(x):0  1  2  3
CD(y)   CD/AB 00 01 11 10
0       00    x  x  x  x
1       01    x  x  x  x
2       11    x  x  x  x
3       10    x  x  x  x
    Args:
        truth_table (list): truth table of vector

    Returns:
        list: list with kmap
    """
    k_map = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    truth_table.pop(0)

    for row in truth_table:
        if not row[4]:
            continue

        k_map[get_coordinate(row, "y")][get_coordinate(row, "x")] = 1

    return k_map
