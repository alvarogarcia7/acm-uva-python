from pprint import pprint
from sys import stdin


def decide(lines: list[str]) -> dict:
    fair_coins = {chr(letter): [False, None] for letter in range(ord('A'), ord('L') + 1)}
    assert len(fair_coins) == 12, len(fair_coins)
    for line in filter(lambda x: x.endswith("even"), lines):
        fair_coin_letters = "".join(line.split(" ")[0:2])
        # all coins in an even are fair
        for letter in fair_coin_letters:
            fair_coins[letter] = [True]

    for line in filter(lambda x: not x.endswith("even"), lines):
        for remaining_letter, value in fair_coins.items():
            # unfair and present in a non-even line: assign weight
            if not value[0] and remaining_letter in line:
                parts = line.split(" ")[0:2]
                if line.endswith("up"):
                    if remaining_letter in parts[0]:
                        result = "heavy"
                    else:
                        result = "light"
                else:
                    if remaining_letter in parts[0]:
                        result = "light"
                    else:
                        result = "heavy"
                fair_coins[remaining_letter][1] = result

    for remaining_letter, value in fair_coins.items():
        # there is only one unfair coin.
        # all unfair candidates that are not present in the weighting, are fair
        if not value[0] and value[1] is None:
            value[0] = True

    unfair_parts = []
    for line in filter(lambda x: not x.endswith("even"), lines):
        if line.endswith("up"):
            unfair_part = 1
        else:
            unfair_part = 0

        unfair_parts.append(line.split(" ")[unfair_part])

    all_unfair_letters = [set(f) for f in unfair_parts]
    if len(all_unfair_letters) > 0:
        res1 = all_unfair_letters[0]
        for x in all_unfair_letters:
            res1 = res1.intersection(x)

        if len(res1) == 1:
            pop = res1.pop()
            for remaining_letter, value in fair_coins.items():
                # there is only one unfair coin.
                # all unfair candidates that are not present in the intersection, are fair
                if remaining_letter == pop:
                    continue
                if not value[0]:
                    fair_coins[remaining_letter] = [True]

    remaining_letters = list(filter(lambda xy: not xy[1][0], fair_coins.items()))
    assert len(remaining_letters) == 1, f"Remaining letters is not 1: {remaining_letters}"
    result = remaining_letters[0]
    return {'coin': result[0], 'status': result[1][1]}


def split_by_cases(lines: list[str]) -> list[list[str]]:
    empty_group = []
    result = [empty_group]
    for line in lines:
        if line == "":
            result.append(empty_group)
        else:
            result[-1].append(line)
    return result


def start(console):
    lines = [line.strip() for line in console.readlines()]
    assert len(lines) > 0, "Lines is empty"

    completed = 0
    total = int(lines[0])
    assert total > 0, "Total of cases must be greater than 0"
    lines.pop(0)

    groups = split_by_cases(lines)

    for group in groups:
        result = decide(group)
        print(f"{result['coin']} is the counterfeit coin and it is {result['status']}.")
        completed += 1

    assert completed == total


if __name__ == '__main__':
    start(stdin)
