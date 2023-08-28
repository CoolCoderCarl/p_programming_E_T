num = int(input("Please input num: "))

prv = 1
cur = 2

for i in range(num + 1):
    nxt = cur + prv
    print(nxt)
    cur = prv
    prv = nxt
