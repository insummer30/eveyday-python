import sys


def get_string_statistics(str_list):
    min_len = sys.maxsize
    max_len = 0
    total_len = 0

    for item in str_list:
        len_str = len(item)
        total_len += len_str

        if len_str > max_len:
            max_len = len_str
        if len_str < min_len:
            min_len = len_str

    avg_len = total_len / len(str_list)

    return min_len, max_len, avg_len


if __name__ == '__main__':
    input_list = ["a", "bb", "ccc", "dddd"]
    print(input_list)
    result = get_string_statistics(input_list)

    print(type(result))
    print(result)
