def get_strings(step, limit):
    word = ''
    temp_count = 0
    char = 'A'
    counter = 0
    while counter < limit:
        if temp_count == step:
            temp_count = 1
            if char == 'A':
                char = 'P'
            else:
                char = 'A'
        else:
            temp_count += 1
        word += char
        counter += 1
    return word


def get_combinations(n):
    """
        Making combinations
    """
    limit = 2 ** n
    str_lst = [get_strings(2**val, limit) for val in range(n)]
    combinations = []
    for i in range(limit):
        value = ''
        for j in range(n):
            value += str_lst[j][i]
        combinations.append(value)
    return combinations


def filter_out_absent(combinations):
    """
        filter out consecutive four days absent
    """
    to_remove_combinations = []
    for combination in combinations:
        splits = combination.split('P')
        for val in splits:
            if val.count('A') >= 4:
                to_remove_combinations.append(combination)
                break
    for combination in to_remove_combinations:
        combinations.remove(combination)
    return combinations


def solution(n):
    combinations = get_combinations(n)
    combinations = filter_out_absent(combinations)
    probability_to_not_attend_count = 0
    for combination in combinations:
        if combination[-1] == 'A':
            probability_to_not_attend_count += 1
    print(
        f"\nfor {n} days: {probability_to_not_attend_count}/{len(combinations)}")


n = input("Please enter value of N:")
n = int(n)
solution(n)
