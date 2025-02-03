def is_degree_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def find_size(kmap: list, number_pos: tuple) -> tuple:
    height = 0
    width = 0
    x_pos, y_pos = number_pos

    # Find height
    for i in range(0, len(kmap)):
        if kmap[(x_pos + i) % len(kmap)][y_pos]:
            height += 1
        else:
            break

    while not is_degree_of_two(height):
        height = height - 1

    # find width
    for i in range(0, len(kmap[0])):
        if kmap[x_pos][(y_pos + i) % len(kmap)]:
            width += 1
        else:
            break

    while not is_degree_of_two(width):
        width = width - 1

    return (height, width)


# FIX v1.1 При обнаружении 0 цикл теперь прерывается,
# а не продолжает искать высоту
def find_island_height(kmap: list, number: tuple, height: int, width: int):
    height_list = []
    for i_w in range(width):

        height_iter = 0

        for i_h in range(height):
            if kmap[
                (number[0] + i_h) % len(kmap)
            ][
                (number[1] + i_w) % len(kmap)
            ]:
                height_iter += 1
            else:
                break  # 1.1 добавлено условие

        while not is_degree_of_two(height_iter):
            height_iter = height_iter - 1

        height_list.append(height_iter)
    return (min(height_list), width)


# FIX v1.1 При обнаружении 0 цикл теперь прерывается,
# а не продолжает искать высоту
def find_island_width(kmap: list, number: tuple, height: int, width: int):
    width_list = []

    for i_h in range(height):

        width_iter = 0

        for i_w in range(width):
            if kmap[
                (number[0] + i_h) % len(kmap)
            ][
                (number[1] + i_w) % len(kmap)
            ]:
                width_iter += 1
            else:
                break

        while not is_degree_of_two(width_iter):
            width_iter -= 1

        width_list.append(width_iter)

    return (height, min(width_list))


def get_all_points(kmap: list, number: tuple, height: int, width: int):
    points = []
    for i_h in range(height):
        for i_w in range(width):
            point = (
                (number[0] + i_h) % len(kmap),
                (number[1] + i_w) % len(kmap[0])
            )
            if kmap[point[0]][point[1]]:
                points.append(point)
    return points


def sort_islands_by_size(islands: list):
    sorted_islands = sorted(
        islands, key=lambda x: x["height"] * x["width"], reverse=True)
    return sorted_islands


def find_minimal_islands_combination(kmap, all_islands):
    all_points_to_cover = set()
    for row in range(len(kmap)):
        for col in range(len(kmap[0])):
            if kmap[row][col] == 1:
                all_points_to_cover.add((row, col))

    selected_islands = []

    while all_points_to_cover:
        best_island = None
        max_covered_points = 0

        for island in all_islands:
            # Считаем количество точек, которые покрывает остров
            covered_points = set(island["points"]) & all_points_to_cover
            if len(covered_points) > max_covered_points:
                best_island = island
                max_covered_points = len(covered_points)

        selected_islands.append(best_island)
        all_points_to_cover -= set(best_island["points"])

    return selected_islands


def find_all_islands(kmap: list) -> dict:
    founded_numbers = []
    islands = []

    for col in range(0, len(kmap)):
        for row in range(0, len(kmap[col])):
            if not kmap[col][row]:
                continue

            founded_numbers.append((col, row))

    # Search islands size
    for number in founded_numbers:
        # Search max square size
        base_height, base_width = find_size(kmap, number)

        vertical_island = find_island_height(
            kmap, number, base_height, base_width)
        horizontal_island = find_island_width(
            kmap, number, base_height, base_width)

        islands.append(
            {
                "height": vertical_island[0],
                "width": vertical_island[1],
                "start_point": number,
                "points": get_all_points(
                    kmap,
                    number,
                    vertical_island[0],
                    vertical_island[1]
                )
            }
        )
        islands.append(
            {
                "height": horizontal_island[0],
                "width": horizontal_island[1],
                "start_point": number,
                "points": get_all_points(
                    kmap,
                    number,
                    horizontal_island[0],
                    horizontal_island[1]
                )
            }
        )

    # Sort islands by size
    sorted_islands = sort_islands_by_size(islands)

    return find_minimal_islands_combination(kmap, sorted_islands)


if __name__ == "__main__":
    kmap_template = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 0, 1]
    ]
    islands = find_all_islands(kmap_template)
    for island in islands:
        print(island)
