S, T = input().split()



if len(T) == 1 or len(S) < len(T):
    print('No')
else:
    div = len(T)

    for k in range(div-1, div + 1):
        t = []
        for i in range(0, len(S), k):
            t.append(S[i:i+k])

        m = []
        for i in range(len(t)):
            if len(t[i]) >= k:
                m.append((t[i])[k-1])

        t = ''.join(m)
        if T == t:
            print('Yes')
            exit(0)

    print('No')
