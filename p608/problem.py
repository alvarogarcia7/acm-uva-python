from pprint import pprint


def decide(lines: list[str]):
    fair_coins = [False for _ in range(0, 11 + 1)]
    assert len(fair_coins) == 12, len(fair_coins)
    for line in lines:
        if line.endswith("even"):
            fair_coin_letters = "".join(line.split(" ")[0:2])
            for letter in fair_coin_letters:
                fair_coins[ord(letter)-ord('A')] = True

    pprint(fair_coins)


def split_by_cases(lines: list[str]) -> list[list[str]]:
    result = [[]]
    for line in lines:
        if line == "":
            result.append([])
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
        decide(group)
        completed += 1

    assert completed == total


if __name__ == '__main__':
    start('input.txt')
