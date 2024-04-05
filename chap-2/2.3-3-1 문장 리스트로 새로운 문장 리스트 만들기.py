def new_str_list(sentence_list):
    word_list = []
    max_word_count = -1

    for sentence in sentence_list:
        words = sentence.split()
        word_list.append(words)
        if len(words) > max_word_count:
            max_word_count = len(words)

    new_word_list = [max_word_count][len(sentence_list)]
    #

    for i in range(0, len(sentence_list)):
        for j in range(0, len(word_list[i])):
            print(f'{word_list[i][j]}')
            new_word_list[j].append(word_list[i][j])

    print(f'{new_word_list}')


if __name__ == '__main__':
    old_str_list = ['aaa bbb ccc', '111 222 333', 'jeong kim park hong']
    # ['aaa 111 jeong', 'bbb 222 kim', ...]
    new_str_list(old_str_list)
