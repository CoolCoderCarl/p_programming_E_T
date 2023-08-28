# Ask for digit to calculate remains
num = int(input("Input digit: "))

if num % 3 == 0:
    print(f"{num} have no remain")
else:
    print(f"Have a {num % 3} remain/s")
