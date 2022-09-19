def sum_only_numbers(input_list):
    total_sum = 0

    for item in input_list:
        try:
            total_sum += int(item)
        except ValueError:
            continue

    return total_sum


if __name__ == '__main__':
    print(sum_only_numbers(["a", 1, 2, "3", "안녕"]))
