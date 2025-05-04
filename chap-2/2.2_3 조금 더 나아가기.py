def fig_latin_start_capital(word):
    additional_dot = ''

    if word[-1] == '.':
        word = word[:-1]
        additional_dot = '.'

    if word[0] in 'aeiouAEIOU':
        print(f'{word}way{additional_dot}')
    else:
        if word[0].isupper() and word[1:].islower():
            print(f'{word[1].upper()}{word[2:]}{word[0].lower()}ay{additional_dot}')
        else:
            print(f'{word[1:]}{word[0]}ay{additional_dot}')


if __name__ == '__main__':
    user_input = input('input word: ')
    fig_latin_start_capital(user_input)
