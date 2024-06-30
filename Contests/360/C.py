N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

cost = 0
bv
tpls = list(zip(A, W))
unique_first_elements = list(set(t[0] for t in tpls))

for i in range(len(unique_first_elements) - 1):
    filtered_tuples = [t for t in tpls if t[0] == unique_first_elements[i]]
    # 最小値を出す
    min_tpls = min(filtered_tuples, key=lambda x: x[1])
    # 箱を一個にする→箱の数だけ掛ける
    cnt = sum(1 for t in tpls if t[0] == min_tpls[0])
    cost += min_tpls[1] * (cnt - 1)

print(cost)