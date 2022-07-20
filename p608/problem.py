def decide(lines: list[str]) -> dict:
    fair_coins = {chr(letter): False for letter in range(ord('A'), ord('L') + 1)}
    assert len(fair_coins) == 12, len(fair_coins)
    for line in filter(lambda x: x.endswith("even"), lines):
        fair_coin_letters = "".join(line.split(" ")[0:2])
        for letter in fair_coin_letters:
            fair_coins[letter] = True

    for line in filter(lambda x: not x.endswith("even"), lines):
        remaining_letters = dict(filter(lambda xy: not xy[1], fair_coins.items()))
        candidate = None
        for remaining_letter in remaining_letters:
            if remaining_letter in line:
                candidate = remaining_letter

        assert candidate is not None
        if line.endswith("up"):
            result = "light"
        else:
            result = "heavy"

        return {'coin': candidate, 'status': result}


def split_by_cases(lines: list[str]) -> list[list[str]]:
    empty_group = []
    result = [empty_group]
    for line in lines:
        if line == "":
            result.append(empty_group)
        else:
            result[-1].append(line)
    return result


def start(file_name):
    lines = []
    with open(file_name, 'r+') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    assert len(lines) > 0, "Lines is empty"

    completed = 0
    total = int(lines[0])
    lines.pop(0)

    groups = split_by_cases(lines)

    for group in groups:
        result = decide(group)
        print(f"{result['coin']} is the counterfeit coin and it is {result['status']}.")
        completed += 1

    assert completed == total


if __name__ == '__main__':
    start('input.txt')
