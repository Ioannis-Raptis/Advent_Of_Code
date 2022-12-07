from input import starting_stacks, rearrangement_procedure


def rearrange(stacks, rearrangement_procedure):
    for number_of_items, from_stack, to_stack in rearrangement_procedure:
        for _ in range(number_of_items):
            stacks[to_stack].append(stacks[from_stack].pop())
    return stacks


def get_top_crates(stacks):
    s = ""
    for key in stacks.keys():
        s += stacks[key].pop()
    return s


# print(get_top_crates(rearrange(starting_stacks, rearrangement_procedure)))

############################## PART 2 ##############################


def rearrange_v2(stacks, rearrangement_procedure):
    for number_of_items, from_stack, to_stack in rearrangement_procedure:
        moving_stack = []
        for _ in range(number_of_items):
            moving_stack.append(stacks[from_stack].pop())
        for item in reversed(moving_stack):
            stacks[to_stack].append(item)
    return stacks


# print(get_top_crates(rearrange_v2(starting_stacks, rearrangement_procedure)))
