import itertools


def find_zero_sum_combinations(ranges):
    # 各範囲内の数値を生成
    lists = [list(range(r[0], r[1] + 1)) for r in ranges]

    # すべての組み合わせを生成して、合計が0になるものを見つける
    result = []
    for combination in itertools.product(*lists):
        if sum(combination) == 0:
            result.append(combination)
    return result


# 数値の範囲を定義 (start, end)
ranges = [(3, 5), (-4, 1), (-2, 3)]

# 0になる組み合わせを見つける
zero_sum_combinations = find_zero_sum_combinations(ranges)

# 結果を表示する
print("Zero sum combinations:")
for combination in zero_sum_combinations:
    print(combination)