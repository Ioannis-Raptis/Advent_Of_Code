from collections import namedtuple

Motion = namedtuple("Motion", ["direction", "steps"])


def get_motions_from_file(file_name):
    motions = []
    with open(file_name) as file:
        for line in file:
            line = line.rstrip()
            motion = Motion(line[0], int(line[2:]))
            motions.append(motion)
        return motions


class Rope:
    def __init__(self) -> None:
        self.head = (0, 0)
        self.tail = (0, 0)
        self.tail_visited_positions = set()

    def move_head(self, direction: str):
        row, column = self.head
        if direction == "R":
            self.head = (row, column + 1)
        elif direction == "U":
            self.head = (row + 1, column)
        elif direction == "L":
            self.head = (row, column - 1)
        elif direction == "D":
            self.head = (row - 1, column)
        else:
            raise ValueError("Invalid direction provided")
        self._update_tail_position()
        return self.head

    def _update_tail_position(self):
        tail_row, tail_column = self.tail
        head_row, head_column = self.head

        row_distance = head_row - tail_row
        column_distance = head_column - tail_column

        right_movement = row_distance == 0 and column_distance == 2
        left_movement = row_distance == 0 and column_distance == -2
        up_movement = row_distance == 2 and column_distance == 0
        down_movement = row_distance == -2 and column_distance == 0

        up_right_movement = (
            row_distance == 2
            and column_distance == 1
            or row_distance == 1
            and column_distance == 2
        )
        down_right_movement = (
            row_distance == -2
            and column_distance == 1
            or row_distance == -1
            and column_distance == 2
        )
        up_left_movement = (
            row_distance == 2
            and column_distance == -1
            or row_distance == 1
            and column_distance == -2
        )
        down_left_movement = (
            row_distance == -2
            and column_distance == -1
            or row_distance == -1
            and column_distance == -2
        )

        if right_movement:
            self.tail = (tail_row, tail_column + 1)
        if left_movement:
            self.tail = (tail_row, tail_column - 1)
        if up_movement:
            self.tail = (tail_row + 1, tail_column)
        if down_movement:
            self.tail = (tail_row - 1, tail_column)

        if up_right_movement:
            self.tail = (tail_row + 1, tail_column + 1)
        if down_right_movement:
            self.tail = (tail_row - 1, tail_column + 1)
        if up_left_movement:
            self.tail = (tail_row + 1, tail_column - 1)
        if down_left_movement:
            self.tail = (tail_row - 1, tail_column - 1)

        self.tail_visited_positions.add(self.tail)


def part_one_solution():
    rope = Rope()
    motions = get_motions_from_file("input.txt")
    for motion in motions:
        for _ in range(motion.steps):
            rope.move_head(motion.direction)
    print(len(rope.tail_visited_positions))


part_one_solution()
