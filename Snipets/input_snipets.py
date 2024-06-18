# 入力内容によって以下の内容で受け取る

# 一行文字列：
# abc
a = input()

# 一行文字列→整数
# 100
a = int(input())

# 二行
# 整数
# 文字列
a = int(input())
b = input()

# 二行
# 整数
# リスト
a = int(input())
b = list(map(int, input().split())) #a:[1,2,3,4,5]

# 一行
# リスト
a = list(map(int, input().split()))