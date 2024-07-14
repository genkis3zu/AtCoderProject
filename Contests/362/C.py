import itertools

N = int(input())
L = []
for i in range(0, N):
    Lx = list(map(int, input().split()))
    L.append(Lx)

SumL0, SumL1 = 0, 0

for i in range(0, N):
    SumL0 += L[i][0]
    SumL1 += L[i][1]

if SumL0 < 0 < SumL1:
    print('Yes')

    # 各範囲内の数値を生成
    lists = [list(range(r[0], r[1] + 1)) for r in L]

    # すべての組み合わせを生成して、合計が0になるものを見つける
    result = []
    for combination in itertools.product(*lists):
        if sum(combination) == 0:
            print(*combination)
            exit(0)

elif (SumL0 == 0 and SumL1 == 0):
    print('No')

else:
    print('No')
