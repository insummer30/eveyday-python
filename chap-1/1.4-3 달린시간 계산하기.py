def run_timing():
    print('Hello')

    total_time_sum = 0
    input_count = 0

    while True:
        user_input = input('Enter 10 km run time: ')

        if not user_input:
            # Exit if nothing to input
            break

        try:
            time = float(user_input)
        except ValueError:
            print('Input only number...')
            continue

        input_count += 1
        total_time_sum += time

    print(f'Avg of {total_time_sum / input_count}, over {input_count} runs')


if __name__ == '__main__':
    run_timing()
