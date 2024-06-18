result = []
now = 1

N, A = map(int, input().split())
t = list(map(int, input().split()))

for i in range(N):
    if i == 0 or (now-1) <= t[i]:
        now = t[i] + A
    else:
        if t[i] <= (t[i-1] + A):
            now += A
        else:
            now += t[i] + A
    result.append(now)

for i in range(N):
    print(result[i])
