M = []

for _ in range(0, 3):
    m = list(map(int, input().split()))
    M.append(m)

ok = True

if M[0][0] - M[0][1] != M[1][0] - M[1][1] or M[1][0] - M[1][1] != M[2][0] - M[2][1]:
    ok = False
elif M[0][1] - M[1][1] != M[1][1] - M[2][1] or M[1][1] - M[2][1] != M[2][1] - M[2][2]:
    ok = False
elif M[0][0] - M[1][0] != M[0][1] - M[1][1] or M[0][1] - M[1][1] != M[0][2] - M[1][2]:
    ok = False

if ok:
    print('Yes')
else:
    print('No')