from main import (
    get_sum_of_calories_of_top_elf,
    get_sum_of_calories_of_top_three_elves,
    get_separate_calories_by_elf,
)

all_calories = [
    1000,
    2000,
    3000,
    "\n",
    4000,
    "\n",
    5000,
    6000,
    "\n",
    7000,
    8000,
    9000,
    "\n",
    10000,
    "\n",
]


def test_should_separate_calories_by_elf():
    assert get_separate_calories_by_elf(all_calories) == [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]


def test_should_get_max_calories_of_an_elf():
    assert (
        get_sum_of_calories_of_top_elf(
            [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
        )
        == 24000
    )


def test_should_get_sum_of_top_three_elf_calories():
    assert (
        get_sum_of_calories_of_top_three_elves(
            [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
        )
        == 45000
    )
