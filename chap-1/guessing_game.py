import random


word_list = ["Banana", "Apple", "Zone", "Car", "Korea"]
sorted_list = sorted(word_list, reverse=True)


def guessing_game():
    print(sorted_list)
    selected_index = random.randint(0, len(sorted_list) - 1)

    while True:
        user_input = input('Guess number (0 ~ 10): ')
        try:
            answer = int(user_input)
        except ValueError:
            print('[Error] Input only digit !!')
            continue

        if answer < 0 or answer > 10:
            print('[Error] Out of input number range !!')
            continue

        if selected_index == answer:
            print(f'Right, is was {sorted_list[answer]}')
            break
        elif selected_index > answer:
            print(f'No, your answer {answer} is too low')
        else:
            print(f'No, your answer {answer} is too high')


if __name__ == '__main__':
    guessing_game()
