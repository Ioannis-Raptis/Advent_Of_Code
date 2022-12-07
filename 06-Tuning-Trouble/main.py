from collections import deque


def get_transmission_from_file(file_name):
    with open(file_name) as file:
        return file.readline()


def get_end_of_starter_marker(transmission, num_of_distinct_characters):
    end_index = num_of_distinct_characters
    q = deque(transmission[:end_index])
    while len(set(q)) != num_of_distinct_characters:
        end_index += 1
        q.popleft()
        q.append(transmission[end_index - 1])
    return end_index


print(get_end_of_starter_marker(get_transmission_from_file("input.txt"), 4))

############################## PART 2 ##############################

print(get_end_of_starter_marker(get_transmission_from_file("input.txt"), 14))
