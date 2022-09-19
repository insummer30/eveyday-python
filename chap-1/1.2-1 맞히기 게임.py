import random


word_list = ["Banana", "Apple", "Zone", "Car", "Korea"]
sorted_list = sorted(word_list, reverse=True)


def guessing_game():
    print(f'This is list: {sorted_list}')
    len_sorted_list = len(sorted_list)
    user_input_msg = f'Guess what word is selected (index 0 ~ {len_sorted_list - 1}): '

    selected_index = random.randint(0, len_sorted_list - 1)

    while True:
        user_input = input(user_input_msg)

        if not user_input.isdigit():
            print("Only input number")
            continue

        try:
            answer = int(user_input)
        except ValueError:
            print('[Error] Input only digit !!')
            continue

        if answer < 0 or answer >= len_sorted_list:
            print('[Error] Out of index range !!')
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
