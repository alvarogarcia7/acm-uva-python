import unittest

from p608.problem import decide


def validate(lines: list[str]):
    mandatory_length = 3
    assert len(lines) == mandatory_length, f"Lines must be of size {mandatory_length}"
    assert all([line.endswith("even") or line.endswith("up") or line.endswith("down") for line in lines])
    return lines


class MyTestCase(unittest.TestCase):
    def test_sample_in_the_description(self):
        input_ = validate("""ABCD EFGH even
ABCI EFJK up
ABIJ EFGH even""".splitlines(False))
        self.assertEqual(decide(input_), {'coin': 'K', 'status': 'light'})

    def test_sample_in_the_description_but_in_the_other_direction(self):
        input_ = validate("""ABCD EFGH even
ABCI EFJK down
ABIJ EFGH even""".splitlines(False))
        self.assertEqual(decide(input_), {'coin': 'K', 'status': 'heavy'})

    def test_sample_by_replacing_final_letters(self):
        input_ = validate("""ABCD EFGH even
ABCI EFJK up
ABIK EFGH even""".splitlines(False))
        self.assertEqual(decide(input_), {'coin': 'J', 'status': 'light'})

    def test_multiple_up(self):
        input_ = validate("""ABCJ EFGH up
ABCI EFJK up
ABIK EFGD even""".splitlines(False))
        self.assertEqual(decide(input_), {'coin': 'J', 'status': 'light'})

    def test_all_down(self):
        input_ = validate("""ABCJ EFGH down
ABCI EFJK down
ABIK EFGD down""".splitlines(False))
        self.assertEqual(decide(input_), {'coin': 'A', 'status': 'light'})


if __name__ == '__main__':
    unittest.main()