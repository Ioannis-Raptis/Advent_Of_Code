from main import Motion, Rope

test_motions = [
    Motion("R", 4),
    Motion("U", 4),
    Motion("L", 3),
    Motion("D", 1),
    Motion("R", 4),
    Motion("D", 1),
    Motion("L", 5),
    Motion("R", 2),
]


def test_should_move_head():
    rope = Rope()
    assert rope.move_head("R") == (0, 1)
    assert rope.move_head("U") == (1, 1)
    assert rope.move_head("L") == (1, 0)
    assert rope.move_head("D") == (0, 0)


def test_tail_should_follow_head():
    rope = Rope()
    rope.move_head("R")
    assert rope.tail == (0, 0)
    rope.move_head("R")
    assert rope.tail == (0, 1)
    rope.move_head("U")
    rope.move_head("U")
    assert rope.tail == (1, 2)


def test_lala():
    rope = Rope()
    for motion in test_motions:
        for _ in range(motion.steps):
            rope.move_head(motion.direction)
