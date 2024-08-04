from itertools import combinations

# 組み合わせ
pairs = [(2, 3), (3, 8), (5, 1), (1, 4)]
x_threshold = 7
y_threshold = 18


# 条件を満たす最小の組み合わせを探す
def find_minimal_combination(pairs, x_threshold, y_threshold):
    n = len(pairs)
    min_size = float('inf')
    min_comb_count = 0

    for i in range(1, n + 1):
        for comb in combinations(pairs, i):
            x_sum = sum(x for x, y in comb)
            y_sum = sum(y for x, y in comb)
            if x_sum <= x_threshold or y_sum <= y_threshold:
                if len(comb) < min_size:
                    min_size = len(comb)
                    min_comb_count = 1
                elif len(comb) == min_size:
                    min_comb_count += 1

    return min_comb_count


# 実行
min_comb_count = find_minimal_combination(pairs, x_threshold, y_threshold)
print(min_comb_count)  # 出力: 1