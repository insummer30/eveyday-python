def generate_nth_sentence(nth):
    """
    words.txt 파일에서 라인 별로 n번째 단어를 골라서 이어 붙여 하나의 문장을 만든다
    """
    f = open('words.txt', 'r')
    nth_words = []
    while True:
        line = f.readline()
        if not line:
            break

        try:
            nth_words.append(line.split()[nth])
        except IndexError:
            continue

    print(f'{" ".join(nth_words)}')

    f.close()


if __name__ == '__main__':
    generate_nth_sentence(2)
