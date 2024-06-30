S = list(input())

if S[0] == 'R':
    print('Yes')
elif S[0] == 'M':
    print('No')
elif S[0] == 'S':
    if S[1] == 'R':
        print('Yes')
    elif S[1] == 'M':
        print('No')
else:
    print('No')
