def get_all_calories_from_file(file_name):
    with open(file_name) as file:
        all_calories = []
        for line in file:
            if line != "\n":
                all_calories.append(int(line.rstrip()))
            else:
                all_calories.append(line)
        all_calories.append("\n")
        return all_calories


def get_separate_calories_by_elf(all_calories: list[int | str]):
    calories_by_elf = []
    sub_list = []
    for calories in all_calories:
        if calories != "\n":
            sub_list.append(calories)
        else:
            calories_by_elf.append(sub_list)
            sub_list = []
    return calories_by_elf


def get_iterator_of_sum_of_calories(calories_by_elf: list[list]):
    return (sum(calories) for calories in calories_by_elf)


def get_sum_of_calories_of_top_elf(calories_by_elf: list[list]):
    return max(get_iterator_of_sum_of_calories(calories_by_elf))


def get_sum_of_calories_of_top_three_elves(calories_by_elf: list[list]):
    iterator = get_iterator_of_sum_of_calories(calories_by_elf)
    return sum(sorted(iterator)[-3:])


def part_one_solution(calories: list[str]):
    print(get_sum_of_calories_of_top_elf(get_separate_calories_by_elf(calories)))


def part_two_solution(calories: list[str]):
    print(
        get_sum_of_calories_of_top_three_elves(get_separate_calories_by_elf(calories))
    )


def main() -> None:
    all_calories = get_all_calories_from_file("input.txt")
    part_one_solution(all_calories)
    part_two_solution(all_calories)


main()
