N, T, P = map(int, input().split())
L = list(map(int, input().split()))

l = sorted(L, reverse=True)

lx = l[0:P]

if T - lx[P - 1] < 0:
    print(0)
else:
    print(T - lx[P - 1])