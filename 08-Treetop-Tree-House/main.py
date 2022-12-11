import numpy as np


def get_map_from_file(file_name):
    with open(file_name) as file:
        map = []
        for line in file:
            row = [height for height in line.rstrip()]
            map.append(row)
    return np.array(map)


def is_tree_visible(tree_height, other_tree_heights):
    if other_tree_heights.size == 0:
        return True
    l = []
    for other_tree in other_tree_heights:
        if other_tree >= tree_height:
            l.append(False)
        else:
            l.append(True)
    return all(l)


def is_visible_from_the_right(tree_height, tree_index_in_row, tree_row):
    other_tree_heights = tree_row[tree_index_in_row + 1 :]
    return is_tree_visible(tree_height, other_tree_heights)


def is_visible_from_the_left(tree_height, tree_index_in_row, tree_row):
    other_tree_heights = tree_row[:tree_index_in_row]
    return is_tree_visible(tree_height, other_tree_heights)


def is_visible_from_the_top(tree_height, tree_index_in_column, tree_column):
    other_tree_heights = tree_column[:tree_index_in_column]
    return is_tree_visible(tree_height, other_tree_heights)


def is_visible_from_the_bottom(tree_height, tree_index_in_column, tree_column):
    other_tree_heights = tree_column[tree_index_in_column + 1 :]
    return is_tree_visible(tree_height, other_tree_heights)


def is_visible(tree_coordinates: tuple, map):
    tree_index_in_column = tree_coordinates[0]
    tree_index_in_row = tree_coordinates[1]

    tree_height = map[tree_index_in_column, tree_index_in_row]

    tree_row = map[tree_index_in_column]
    tree_column = map[:, tree_index_in_row]

    if is_visible_from_the_right(tree_height, tree_index_in_row, tree_row):
        return True
    if is_visible_from_the_left(tree_height, tree_index_in_row, tree_row):
        return True
    if is_visible_from_the_top(tree_height, tree_index_in_column, tree_column):
        return True
    if is_visible_from_the_bottom(tree_height, tree_index_in_column, tree_column):
        return True

    return False


def get_number_of_visible_trees(map):
    it = np.nditer(map, flags=["multi_index"])
    return sum(is_visible((it.multi_index[0], it.multi_index[1]), map) for _ in it)


def part_one_solution():
    print(get_number_of_visible_trees(get_map_from_file("input.txt")))


############################## PART 2 ##############################
def get_viewing_distance(tree_height, other_tree_heights):
    if other_tree_heights.size == 0:
        return 0
    viewing_distance = 0
    for other_tree in other_tree_heights:
        if other_tree >= tree_height:
            viewing_distance += 1
            return viewing_distance
        else:
            viewing_distance += 1
    return viewing_distance


def get_viewing_distance_v2(tree_height, other_tree_heights):
    if other_tree_heights.size == 0:
        return 0
    viewing_distance = 0
    for other_tree in reversed(other_tree_heights):
        if other_tree >= tree_height:
            viewing_distance += 1
            return viewing_distance
        else:
            viewing_distance += 1
    return viewing_distance


def get_viewing_distance_to_the_right(tree_height, tree_index_in_row, tree_row):
    other_tree_heights = tree_row[tree_index_in_row + 1 :]
    return get_viewing_distance(tree_height, other_tree_heights)


def get_viewing_distance_to_the_left(tree_height, tree_index_in_row, tree_row):
    other_tree_heights = tree_row[:tree_index_in_row]
    return get_viewing_distance_v2(tree_height, other_tree_heights)


def get_viewing_distance_to_the_top(tree_height, tree_index_in_column, tree_column):
    other_tree_heights = tree_column[:tree_index_in_column]
    return get_viewing_distance_v2(tree_height, other_tree_heights)


def get_viewing_distance_to_the_bottom(tree_height, tree_index_in_column, tree_column):
    other_tree_heights = tree_column[tree_index_in_column + 1 :]
    return get_viewing_distance(tree_height, other_tree_heights)


def get_viewing_distances(tree_coordinates: tuple, map):
    tree_index_in_column = tree_coordinates[0]
    tree_index_in_row = tree_coordinates[1]

    tree_height = map[tree_index_in_column, tree_index_in_row]

    tree_row = map[tree_index_in_column]
    tree_column = map[:, tree_index_in_row]

    return (
        get_viewing_distance_to_the_top(tree_height, tree_index_in_column, tree_column),
        get_viewing_distance_to_the_left(tree_height, tree_index_in_row, tree_row),
        get_viewing_distance_to_the_right(tree_height, tree_index_in_row, tree_row),
        get_viewing_distance_to_the_bottom(
            tree_height, tree_index_in_column, tree_column
        ),
    )


def get_viewing_distance_score(viewing_distances: tuple):
    top, left, right, bottom = viewing_distances
    return top * left * right * bottom


def part_two_solution():
    map = get_map_from_file("input.txt")
    it = np.nditer(map, flags=["multi_index"])
    viewing_distances_list = [
        get_viewing_distances((it.multi_index[0], it.multi_index[1]), map) for _ in it
    ]
    print(
        max(
            [
                get_viewing_distance_score(viewing_distances)
                for viewing_distances in viewing_distances_list
            ]
        )
    )


part_two_solution()
