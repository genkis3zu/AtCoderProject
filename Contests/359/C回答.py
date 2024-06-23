Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

# タイルの左側に寄せておく
if (Sx + Sy) % 2 == 1:
    Sx -= 1
if (Tx + Ty) % 2 == 1:
    Sx -= 1

# 答えは (|Sy - Ty| + max(|Sx - Tx|, |Sy - Ty|)) / 2
Dx = abs(Sx - Tx)
Dy = abs(Sy - Ty)

print((Dy + max(Dx, Dy)) // 2)

# y≥x なら右方向の移動が不要なため
# y 回、そうでないなら右方向に
# (x−y)/2 回（この値は整数です）の移動が必要なため
# y+(x−y)/2 回です

Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

Sx -= (Sy - Sx) % 2
Tx -= (Ty - Tx) % 2

Tx -= Sx
Ty -= Sy

Tx = abs(Tx)
Ty = abs(Ty)

print(Ty + max(0, Tx - Ty) // 2)
