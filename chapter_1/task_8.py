# Ask for range
num = int(input("Please input num: "))

# Var to store previous digit in Fibonacci subsequence
prv = 1
# Var to store current digit in Fibonacci subsequence
cur = 2

for i in range(num + 1):
    # Var to calculate next digit in Fibonacci subsequence
    nxt = cur + prv
    print(nxt)
    cur = prv
    prv = nxt
