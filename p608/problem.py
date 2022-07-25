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

    # if a line is not even, the unfair coin is present
    # all coins that are not present are fair
    for line in filter(lambda x: not x.endswith("even"), lines):
        letters_that_are_present = "".join(line.split(" ")[0:2])
        for letter, value in fair_coins.items():
            if letter not in letters_that_are_present:
                fair_coins[letter] = [True]

    parts_for_group_1 = []
    parts_for_group_2 = []
    for line in filter(lambda x: not x.endswith("even"), lines):
        if line.endswith("up"):
            group_1 = 1
            group_2 = 0
        else:
            group_1 = 0
            group_2 = 1

        assert (group_1 + group_2) == 1

        parts_for_group_1.append(line.split(" ")[group_1])
        parts_for_group_2.append(line.split(" ")[group_2])

    # The unfair, if present, must be in all the weights that are unfair
    all_unfair_letters = intersection_of_all(parts_for_group_1) + intersection_of_all(parts_for_group_2)
    if len(all_unfair_letters) == 1:
        pop = all_unfair_letters.pop()
        for remaining_letter, value in fair_coins.items():
            # there is only one unfair coin.
            # all unfair candidates that are not present in the intersection, are fair
            if remaining_letter == pop:
                continue
            if not value[0]:
                fair_coins[remaining_letter] = [True]

    remaining_letters = list(filter(lambda xy: not xy[1][0], fair_coins.items()))
    assert len(remaining_letters) == 1, f"Remaining letters is not 1, but {len(remaining_letters)}: {remaining_letters}"
    result = remaining_letters[0]
    return {'coin': result[0], 'status': result[1][1]}


def intersection_of_all(parts):
    all_unfair_letters = [set(f) for f in parts]
    result = set()
    if len(all_unfair_letters) > 0:
        result = all_unfair_letters[0]
        for x in all_unfair_letters:
            result = result.intersection(x)
    return list(result)

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
