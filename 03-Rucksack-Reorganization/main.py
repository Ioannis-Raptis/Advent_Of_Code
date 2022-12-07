import string
from itertools import zip_longest


def get_list_of_rucksack_contents_from_file(file_name):
    with open(file_name) as file:
        list_of_rucksack_contents = []
        for line in file:
            line = line.rstrip()
            list_of_rucksack_contents.append(line)
        return list_of_rucksack_contents


def get_item_type_in_both_compartments(rucksack_contents):
    s = int(len(rucksack_contents) / 2)
    compartment_a = rucksack_contents[s:]
    compartment_b = rucksack_contents[:s]
    return set(compartment_a).intersection(compartment_b).pop()


def get_item_type_priority(item_type):
    item_types = string.ascii_letters
    for idx, x in enumerate(item_types):
        if item_type == x:
            return idx + 1


# list_of_rucksack_contents = get_list_of_rucksack_contents_from_file("input.txt")
# print(sum(get_item_type_priority(get_item_type_in_both_compartments(rucksack_contents)) for rucksack_contents in list_of_rucksack_contents))

############################## PART 2 ##############################


def get_group_badge(group_rucksack_contents):
    return (
        set(group_rucksack_contents[0])
        .intersection(group_rucksack_contents[1])
        .intersection(group_rucksack_contents[2])
        .pop()
    )


# Got this from itertools recipes
def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    else:
        raise ValueError("Expected fill, strict, or ignore")


# list_of_rucksack_contents = get_list_of_rucksack_contents_from_file("input.txt")
# print(
#     sum(
#         get_item_type_priority(get_group_badge(group_rucksack_contents))
#         for group_rucksack_contents in grouper(list_of_rucksack_contents, 3)
#     )
# )
