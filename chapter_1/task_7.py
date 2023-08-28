# Ask for digit for range limit to calculate factorial
num = int(input("Please input positive num: "))

fac = 1
if num > 0:
    for i in range(1, num + 1):
        fac = fac * i
        print(fac)
