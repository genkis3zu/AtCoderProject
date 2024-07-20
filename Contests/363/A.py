R = int(input())
result = 0

if 1 <= R <= 99:
    result = 100 - R
elif 100 <= R <= 199:
    result = 200 - R
elif 200 <= R <= 299:
    result = 300 - R
elif 300 < R <= 399:
    result = 400 - R

print(result)