def get_list_of_section_assignment_pairs_from_file(file_name):
    with open(file_name) as file:
        list_of_section_assignment_pairs = []
        for line in file:
            line = tuple(line.rstrip().split(","))
            list_of_section_assignment_pairs.append(line)
        return list_of_section_assignment_pairs


def get_range_sections(section_range: str):
    range_start = int(section_range.split("-")[0])
    range_end = int(section_range.split("-")[1]) + 1
    range_sections = range(range_start, range_end)
    return set(range_sections)


def one_range_contains_the_other(range_pair: tuple[str]):
    range_a = get_range_sections(range_pair[0])
    range_b = get_range_sections(range_pair[1])
    return range_b.issubset(range_a) or range_a.issubset(range_b)


list_of_section_assignment_pairs = get_list_of_section_assignment_pairs_from_file(
    "input.txt"
)

# print(
#     sum(
#         [
#             one_range_contains_the_other(section_assignment_pair)
#             for section_assignment_pair in list_of_section_assignment_pairs
#         ]
#     )
# )

############################## PART 2 ##############################


def ranges_overlap(range_pair: tuple[str]):
    range_a = get_range_sections(range_pair[0])
    range_b = get_range_sections(range_pair[1])
    common_elements = range_a.intersection(range_b)
    return True if common_elements else False


# print(
#     sum(
#         [
#             ranges_overlap(section_assignment_pair)
#             for section_assignment_pair in list_of_section_assignment_pairs
#         ]
#     )
# )
