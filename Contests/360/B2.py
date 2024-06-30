S, T = input().split()

if len(T) == 1 or len(S) < len(T):
    print('No')
else:

    for b in range(0, len(T)):
        div = int((len(S) - b ) / len(T))

        t = []
        for i in range(0, len(S), div):
            t.append(S[i:i+div])

        m = []
        for i in range(len(t)):
            if len(t[i]) >= div:
                m.append((t[i])[div-1])

        t = ''.join(m)
        if T == t:
            print('Yes')
            exit(0)

    print('No')
