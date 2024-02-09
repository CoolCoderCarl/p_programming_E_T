f_digit = int(input("Input first digit:"))
s_digit = int(input("Input second digit:"))
t_digit = int(input("Input third digit:"))

fixed_digit = 2

if f_digit + fixed_digit == s_digit and s_digit + fixed_digit == t_digit:
    print("It is sequence")
else:
    print("It is not sequence")