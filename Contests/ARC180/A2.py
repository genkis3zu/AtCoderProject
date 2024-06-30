#ARC180 A問題

N = int(input())
S = input()

result = 0

def count_possible_strings(S):
    mod = 10**9 + 7
    results = set([S])
    current_set = {S}

    while current_set:
        next_set = set()
        for s in current_set:
            idx = 0
            while "ABA" in s[idx:]:
                pos = s.find("ABA", idx)
                new_s = s[:pos] + "A" + s[pos+3:]
                if new_s not in results:
                    next_set.add(new_s)
                idx = pos + 1

            idx = 0
            while "BAB" in s[idx:]:
                pos = s.find("BAB", idx)
                new_s = s[:pos] + "B" + s[pos+3:]
                if new_s not in results:
                    next_set.add(new_s)
                idx = pos + 1

        results.update(next_set)
        current_set = next_set

    return len(results) % mod

# 例
result = count_possible_strings(S)
print(result)
