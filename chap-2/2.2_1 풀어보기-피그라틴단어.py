def make_pig_latin_word(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'


def pig_latin_word(word):
    print(make_pig_latin_word(word))


def pig_latin_sentence(sentence):
    """
    문장을 받아서 피그 라틴어 적용하기
    """
    new_words = []
    for word in sentence.split():
        new_words.append(make_pig_latin_word(word))

    print(f'{" ".join(new_words)}')


if __name__ == '__main__':
    user_input = input('Input word: ')
    pig_latin_word(user_input)

    user_sentence = input('Input sentence: ')
    pig_latin_sentence(user_sentence)
