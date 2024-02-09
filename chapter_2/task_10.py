a_digit = int(input("Input A digit:"))
b_digit = int(input("Input B digit:"))

try:
    if a_digit != 0:
        x = (b_digit - 1)/a_digit - 1
        print(x)
    elif a_digit == 0 and b_digit == 1:
        print("Solution is any digits")
    elif a_digit == 0 and b_digit != 1:
        print("The equation has no solution")
except BaseException as base_err:
    print(base_err)
