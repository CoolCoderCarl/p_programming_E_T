f_digit = int(input("Input first digit:"))
s_digit = int(input("Input second digit:"))
t_digit = int(input("Input third digit:"))


if f_digit + s_digit > t_digit and s_digit + t_digit > f_digit and f_digit + t_digit > s_digit:
    print("It is triangle")
else:
    print("It is not triangle")