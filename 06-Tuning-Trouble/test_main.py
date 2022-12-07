from main import get_end_of_starter_marker


def test_should_get_end_of_starter_marker():
    assert get_end_of_starter_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert get_end_of_starter_marker("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert get_end_of_starter_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert get_end_of_starter_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11
