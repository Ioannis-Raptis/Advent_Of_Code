from collections import deque

import pytest
from main import get_top_crates, rearrange


@pytest.fixture
def test_starting_stacks():
    return {
        1: deque(["Z", "N"]),
        2: deque(["M", "C", "D"]),
        3: deque(["P"]),
    }


test_rearrangement_procedure = [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]


def test_should_rearrange_stacks_to_procedure(test_starting_stacks):
    assert rearrange(test_starting_stacks, test_rearrangement_procedure) == {
        1: deque(["C"]),
        2: deque(["M"]),
        3: deque(["P", "D", "N", "Z"]),
    }


def test_should_get_top_crates(test_starting_stacks):
    assert get_top_crates(test_starting_stacks) == "NDP"
