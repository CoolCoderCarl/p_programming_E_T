f_digit = int(input("Input first digit:"))
s_digit = int(input("Input second digit:"))

try:
    print(f"{f_digit} > {s_digit}") if f_digit > s_digit else print(f"{s_digit} > {f_digit}")
except BaseException as base_err:
    print(base_err)
