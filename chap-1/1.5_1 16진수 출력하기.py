# 16진수 숫자를 입력 받아서 10진수로 변환하여 출력하기

def hex_output():
    print('첫번째 프로그램 입니다.')
    user_input = input('16진수 숫자 입력: ')

    converted_number = 0

    for idx, value in enumerate(reversed(user_input)):
        converted_number += int(value) * (16 ** idx)

    print(f'변환된 값: {converted_number}')


def hex_output_with_ord():
    print('두번째 프로그램 입니다.')
    user_input = input('16진수 숫자 입력: ')

    converted_number = 0

    for idx, value in enumerate(reversed(user_input)):
        converted_number += (ord(value) - ord("0")) * (16 ** idx)

    print(f'변환된 값: {converted_number}')


if __name__ == '__main__':
    hex_output()
    hex_output_with_ord()
