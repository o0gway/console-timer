import time
import os
import winsound
from random import randint
import json


# Clear console after start timer
def clear_console():
    os.system('cls||clear')


# start program
def main():
    # Flag control for repeat program
    flag_quit = True
    # Flag repeat last timer
    flag_repeat = False

    while flag_quit:
        answer_repeat = input('Хотите использовать ранее уставноленное время(Y/N)?' ).lower()
        if answer_repeat == 'y':
            with open('last_timer.json') as file:
                last_timer = json.load(file)
        else:
            # init dict last_timer
            last_timer = {}
            # Validate parameters
            try:
                last_timer['hours'] = int(input('Пожалуйста введите часы: '))
                last_timer['minutes'] = int(input('Пожалуйста введите минуты(0-59): '))
                if last_timer['minutes'] < 0 or last_timer['minutes'] > 59:
                    print('Введите правильное значение')
                    continue
                last_timer['seconds'] = int(input('Пожалуйста введите секунды(0:59): '))
                if last_timer['seconds'] < 0 or last_timer['seconds'] > 59:
                    print('Введите правильное значение')
                    continue
            except ValueError:
                print('Введите правильное значение')
                continue

            # write last_time
            with open('last_timer.json', 'w') as file:
                json.dump(last_timer, file)

        # random sound for timer
        random_sound = randint(1, 12)

        # Start clear console
        clear_console()
        for hour in range(last_timer['hours'], -1, -1):
            for minute in range(last_timer['minutes'], -1, -1):
                for second in range(last_timer['seconds'], -1, -1):
                    print(hour, ':', minute, ':', second, end='\r')
                    time.sleep(1)
                    if second == 10:
                        clear_console()
                else:
                    clear_console()
                    last_timer['seconds'] = 59
            else:
                last_timer['minutes'] = 59

        print('Ваше время истекло...')
        # Start alarm timer
        for _ in range(3):
            winsound.PlaySound(os.path.join(f"media/{random_sound}.wav"), winsound.SND_FILENAME)
            time.sleep(3)



        # Check user choice for repeat timer
        answer = input('Запустить таймер еще раз(Y/N)?: ').lower()
        if answer == 'n':
            flag_quit = False


main()
