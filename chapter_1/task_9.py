import random

# Generate random list
task_list_9 = [random.randint(1, 100) for k in range(10)]
print(task_list_9)
def find_second_max_dig(list_to_find: list) -> int:
    """
    Find second max digit in the list
    :param list_to_find:
    :return:
    """
    return list(sorted(list_to_find))[-2]


if __name__ == "__main__":
    find_second_max_dig(task_list_9)
