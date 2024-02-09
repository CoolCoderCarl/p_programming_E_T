input_digits = list(input("Input digits to exclude: "))
upper_limit = input("Input upper limit: ")
result = 0

exclude_digits = list(map(int, input_digits))

for i in range(int(upper_limit) + 1):
    if i in exclude_digits:
        continue
    else:
        result += i

print(result)
