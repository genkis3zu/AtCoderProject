#ARC180 A問題

N = int(input())
S = input()
M = []

M.append(S)

# S自体が1
cnt = 1

def add_unique_string(string_list, new_string):
    if new_string not in string_list:
        return True  # 追加に成功
    else:
        return False  # すでに存在

def count_aba_matches(s, m, c):

    aba = s.replace('ABA', 'A', 1)
    if aba != s and add_unique_string(m, aba):
        c += 1
        m.append(aba)
        m, c = count_aba_matches(aba, m, c)

    return m, c

def count_bab_matches(s, m, c):
    bab = s.replace('BAB', 'B', 1)
    if bab != s and add_unique_string(m, bab):
        c += 1
        m.append(bab)
        m, c = count_bab_matches(bab, m, c)

    return m, c


for i in range(0, N - 4):
    M, cnt = count_aba_matches(S, M, cnt)
    M, cnt = count_bab_matches(S, M, cnt)

print(M)
print(cnt % (10 ^ 9 + 7))
