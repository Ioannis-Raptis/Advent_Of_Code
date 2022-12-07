from main import one_range_contains_the_other, get_range_sections, ranges_overlap


list_of_section_assignment_pairs = [
    ("2-4", "6-8"),
    ("2-3", "4-5"),
    ("5-7", "7-9"),
    ("2-8", "3-7"),
    ("6-6", "4-6"),
    ("2-6", "4-8"),
]


def test_should_get_range_sections():
    assert get_range_sections("2-8") == {2, 3, 4, 5, 6, 7, 8}
    assert get_range_sections("9-12") == {9, 10, 11, 12}


def test_should_get_if_one_range_contains_the_other():
    assert one_range_contains_the_other(("2-8", "3-7")) == True
    assert one_range_contains_the_other(("2-6", "4-8")) == False


def test_should_get_if_ranges_overlap():
    assert ranges_overlap(("2-4","6-8")) == False
    assert ranges_overlap(("2-6", "4-8")) == True
