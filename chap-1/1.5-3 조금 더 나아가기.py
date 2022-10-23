# 이름 삼각형 만들기

def make_name_triangle():
    input_name = input('이름을 입력 해주세요: ')

    for idx, one_word in enumerate(input_name):
        print(f'{input_name[:idx + 1]}')


if __name__ == '__main__':
    make_name_triangle()
