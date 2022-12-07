from main import (
    get_item_type_in_both_compartments,
    get_item_type_priority,
    get_group_badge,
)


rucksack_contents_tuple = (
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
)


def test_should_get_item_type_in_both_compartments():
    assert get_item_type_in_both_compartments("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
    assert get_item_type_in_both_compartments("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert get_item_type_in_both_compartments("PmmdzqPrVvPwwTWBwg") == "P"
    assert get_item_type_in_both_compartments("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == "v"


def test_should_get_item_type_priority():
    assert get_item_type_priority("p") == 16
    assert get_item_type_priority("L") == 38


def test_should_get_group_badge():
    assert get_group_badge(rucksack_contents_tuple[:3]) == "r"
    assert get_group_badge(rucksack_contents_tuple[3:]) == "Z"
