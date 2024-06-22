N = int(input())

M = []

for _ in range(0, N):
    si = input()
    si = list(si)
    M.append(si)

for i in range(N - 2, -1, -1):
    for j in range(1, 2*N-2):
        if M[i][j] == '#':
            if M[i][j-1] == 'X':
                M[i][j] = 'X'
            elif M[i][j] == 'X':
                M[i][j] = 'X'
            elif M[i][j+1] == 'X':
                M[i][j] = 'X'

for i in range(0, N):
    M[i] = ''.join(M[i])
    print(M[i])
