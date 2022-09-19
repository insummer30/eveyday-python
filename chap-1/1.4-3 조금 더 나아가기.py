from decimal import Decimal


def print_float_before_after_dot(input_num, before, after):
    """
    소수점을 기준으로 before 수 만큼과 after 수 만큼 앞 뒤 잘라서 출력하기
    """
    float_str = str(input_num)
    dot_idx = float_str.index(".")

    print(f'Original: {float_str}')
    print(f'Processed: {float_str[dot_idx - before:dot_idx] + float_str[dot_idx: dot_idx + 1 + after]}')


def accurate_add_float_numbers(num_str1, num_str2):
    """
    파이썬에서 정확한 소수점 계산을 위해 제공되는 decimal 모듈을 사용해서 덧셈을 수행
    """
    decimal1 = Decimal(num_str1)
    decimal2 = Decimal(num_str2)

    print(f'Decimal sum is {decimal1 + decimal2}')
    pass


if __name__ == '__main__':
    print_float_before_after_dot(123.4567, 2, 3)
    accurate_add_float_numbers('0.1', '0.2')
