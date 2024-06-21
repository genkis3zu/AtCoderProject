# Bingoゲーム

# 入力部分
A = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    A.append(row)

# 判定用のテーブルを作る
# M = [[False, False, False], [False, False, False], [False, False, False]]
M = []
for i in range(0,3):
    row = []
    for j in range(0,3):
        row.append(False)

    M.append(row)

# 各数字で、判定用テーブルを更新する
N = int(input())

for _ in range(0, N):
    b = int(input())

    for i in range(0,3):
        for j in range(0,3):

            if A[i][j] == b:
                M[i][j] = True

# ビンゴを達成しているかどうかを調べる
bingo = False

for i in range(0,3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0,3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print('Yes')
else:
    print('No')