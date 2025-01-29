def minimize_dnf(islands):
    minimized_dnf = ""
    points_list = [[0, 0], [0, 1], [1, 1], [1, 0]]

    for island in islands:
        island_to_boolean_function = {
            "A": [],
            "B": [],
            "C": [],
            "D": []
        }
        for point in island["points"]:
            cd = points_list[point[0]]
            ab = points_list[point[1]]

            island_to_boolean_function["A"].append(ab[0])
            island_to_boolean_function["B"].append(ab[1])
            island_to_boolean_function["C"].append(cd[0])
            island_to_boolean_function["D"].append(cd[1])

        temp_str = ""
        for key in island_to_boolean_function:
            if (
                    0 in island_to_boolean_function[key]
                    and
                    1 in island_to_boolean_function[key]):
                pass
            elif 0 in island_to_boolean_function[key]:
                temp_str += f"{key}'"
            elif 1 in island_to_boolean_function[key]:
                temp_str += f"{key}"

        minimized_dnf += temp_str

        if island != islands[-1]:
            minimized_dnf += " + "
    return minimized_dnf
