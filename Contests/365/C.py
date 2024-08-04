N, M = map(int, input().split())
A = list(map(int, input().split()))

if int(M/N) > len(A):
    print('infinite')
    exit()

for i in range(int(M/N)+2):
    total = sum(min(i,x) for x in A)
    if total > M:
        print(i-1)
        exit()