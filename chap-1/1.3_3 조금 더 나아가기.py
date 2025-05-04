import sys


def get_string_statistics(str_list):
    """
    문자열 리스트를 받아서 최소, 최대, 평균 길이를 튜플로 반환하는 함수
    """
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


def sum_only_numbers(input_list):
    """
    입력 받은 리스트에서 숫자로 변환 가능한 것만 더하기
    """
    total_sum = 0

    for item in input_list:
        try:
            total_sum += int(item)
        except ValueError:
            continue

    return total_sum


if __name__ == '__main__':
    # 1
    input_list = ["a", "bb", "ccc", "dddd"]
    result = get_string_statistics(input_list)
    print(result)

    # 2
    print(sum_only_numbers(["a", 1, 2, "3", "안녕"]))
