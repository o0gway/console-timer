import time
import os
import winsound
from random import randint


# Clear console after start timer
def clear_console():
    os.system('cls||clear')


# start program
def main():
    # Flag control for repeat program
    flag = True
    while flag:
        try:
            hours = int(input('Пожалуйста введите часы: '))
            minutes = int(input('Пожалуйста введите минуты(0-59): '))
            if minutes < 0 or minutes > 59:
                print('Введите правильное значение')
                continue
            seconds = int(input('Пожалуйста введите секунды(0:59): '))
            if seconds < 0 or seconds > 59:
                print('Введите правильное значение')
                continue
        except ValueError:
            print('Введите правильное значение')
            continue

        # random sound for timer
        random_sound = randint(1, 15)

        # Start clear console
        clear_console()
        for hour in range(hours, -1, -1):
            for minute in range(minutes, -1, -1):
                for second in range(seconds, -1, -1):
                    print(hour, ':', minute, ':', second, end='\r')
                    time.sleep(1)
                    if second == 10:
                        clear_console()
                else:
                    clear_console()
                    seconds = 59
            else:
                minutes = 59

        print('Ваше время истекло...')
        # Start alarm timer
        for _ in range(3):
            winsound.PlaySound(os.path.join(f"media/{random_sound}.wav"), winsound.SND_FILENAME)
            time.sleep(3)

        # Check user choice for repeat timer
        answer = input('Запустить таймер еще раз(Y/N)?: ').lower()
        if answer == 'n':
            flag = False


main()
