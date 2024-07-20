N, T, P = map(int, input().split())
L = list(map(int, input().split()))

p = len([num for num in L if num >= T])
cnt = 0
if p >= P:
    print(0)
    exit()

l = L.copy()
while p <= P:
    l = [num + 1 for num in l]
    p = len([num for num in l if num >= T])
    cnt += 1

print(cnt - 1)