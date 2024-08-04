N = int(input())
A = list(map(int, input().split()))


def second_largest_index(lst):
    if len(lst) < 2:
        return None  # 要素数が2未満の場合、2番目に大きい値は存在しない

    first, second = float('-inf'), float('-inf')
    first_index, second_index = -1, -1

    for i, value in enumerate(lst):
        if value > first:
            second, second_index = first, first_index
            first, first_index = value, i
        elif value > second and value != first:
            second, second_index = value, i

    return second_index

print(second_largest_index(A)+1)