S = input()

na = 0
nb = 0
nc = 0
for x in S:
    if x == "a":
        na += 1
    elif x == "b":
        nb += 1
    elif x == "c":
        nc += 1

# もしくは
na = S.count("a")
nb = S.count("b")
nc = S.count("c")