# Map
H, W = map(int, input().split())
# 現在地
Sh, Sw = map(int, input().split())

Sh -= 1
Sw -= 1

# Map info
C = []
for i in range(H):
    C.append(list(input()))

# Description
X = list(input())

def move(Sh, Sw, i):
    if i == 'L':
        if Sw > 0:
            if C[Sh][Sw - 1] == '.':
                Sw -= 1
    elif i == 'R':
        if Sw < W - 1:
            if C[Sh][Sw + 1] == '.':
                Sw += 1
    elif i == 'U':
        if Sh > 0:
            if C[Sh - 1][Sw] == '.':
                Sh -= 1
    elif i == 'D':
        if Sh < H - 1:
            if C[Sh + 1][Sw] == '.':
                Sh += 1

    return Sh, Sw

#print(Sh, Sw)

for i in range(len(X)):
    Sh, Sw = move(Sh, Sw, X[i])
    #print(Sh, Sw)

print(Sh + 1, Sw + 1)
