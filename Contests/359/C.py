SX, SY = map(int, input().split())
TX, TY = map(int, input().split())

cost = 0

# 移動する量を決定する
X = SX - TX
Y = SY - TY

# 現在地
CX = SX
CY = SY

if X == 0:
    cost = abs(Y)
elif Y == 0:
    cost = abs(X % 2) - 1
elif abs(Y) < abs(X):
    costX = abs((X % 2) - Y - 1)
    costY = abs(Y)
    cost = costX + costY
else:
    cost = abs(Y)

print(cost)
