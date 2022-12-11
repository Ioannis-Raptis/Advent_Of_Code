import numpy as np
from main import get_number_of_visible_trees, get_viewing_distance_score, get_viewing_distances, is_visible


test_heightmap = np.array(
    [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]
)


def test_should_check_if_tree_is_visible():
    assert is_visible((0, 1), test_heightmap) == True
    assert is_visible((2, 2), test_heightmap) == False
    assert is_visible((0, 0), test_heightmap) == True
    assert is_visible((4, 4), test_heightmap) == True
    assert is_visible((3, 1), test_heightmap) == False
    assert is_visible((1, 1), test_heightmap) == True
    assert is_visible((3, 3), test_heightmap) == False


def test_should_get_number_of_visible_trees():
    assert get_number_of_visible_trees(test_heightmap) == 21


def test_should_get_viewing_distances():
    assert get_viewing_distances((1, 2), test_heightmap) == (1, 1, 2, 2)
    assert get_viewing_distances((3, 2), test_heightmap) == (2, 2, 2, 1)


def test_should_get_viewing_distance():
    assert get_viewing_distance_score((1, 1, 2, 2)) == 4
    assert get_viewing_distance_score((2, 2, 2, 1)) == 8
