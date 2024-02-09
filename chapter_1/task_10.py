def calculate_sum_odd_digits(digit_count: int) -> int:
    """
    Calculate sum of odd digits in range and return
    :param digit_count:
    :return:
    """
    i = 0
    for i in range(digit_count):
        if i % 2 == 0:
            pass
        else:
            i += i
    return i


if __name__ == "__main__":
    print(calculate_sum_odd_digits(10))
