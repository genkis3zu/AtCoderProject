N = int(input())
flg = 0
for i in range(N):
    S = input()
    if S == 'sweet':
        flg += 1
    else:
        if flg > 0:
            flg -= 1
        else:
            flg = 0

    if flg == 2 and i != N - 1:
        print('No')
        exit()
    if flg > 2:
        print('No')
        exit()

print('Yes')
