def my_sum(*numbers):
    total_sum = numbers[1]
    for i in numbers[0]:
        total_sum += i

    print(f'Total sum is {total_sum}')
    return total_sum


def my_avg(number_list):
    total_sum = my_sum(number_list, 0)
    print(f'Avg is {total_sum / len(number_list)}')


if __name__ == '__main__':
    my_avg([1, 2, 3, 5])
