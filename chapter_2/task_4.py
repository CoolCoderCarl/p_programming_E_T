list_1 = [1, 2, 3, 5]
list_2 = [1, 2, 3, 5]

if len(list_1) == len(list_2):
    for i in range(len(list_1)):
        if list_1[i] == list_2[i]:
            print(f"{list_1[i]} = {list_2[i]}")
        else:
            print(f"{list_1[i]} != {list_2[i]}")
else:
    print("Lists length are not equal!")
