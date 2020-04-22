from datetime import timedelta
from datetime import datetime

today_date = datetime.today()
default_time = 25
timeout_time = timedelta(seconds=default_time)


def display_menu():
    """
    Formats and prints the main menu to the screen.
    """
    greeting = "    POMODORO TIMER    "
    greeting_time = f'    {today_date.ctime()}    '
    menu = ['MAIN MENU:', f'1. Set Timeout - current: {timeout_time}', '2. Start Timer']

    print(''.center(100, '-'))
    print(greeting.center(100, '*'))
    print(greeting_time.center(100, '*'))
    print(''.center(100, '-'))
    print('\n')
    # print menu options
    for item in menu:
        print(item.center(100))
    print('\n')


def countdown():
    """
    displays a countdown timer with the timeout variable that counts down to 0 then prints out message when done.
    """
    start_time = datetime.today()
    start_time_string = start_time.time().strftime('%H:%M:%S')
    end_time = start_time + timeout_time
    end_time_string = end_time.time().strftime('%H:%M:%S')
    print(''.center(100, '-'))
    print(f'    Start time: {start_time_string}    '.center(100, '*'))
    print(f'    End time: {end_time_string}    '.center(100, '*'))
    print(''.center(100, '-'))
    print()

    while True:
        now = datetime.today().time().strftime('%H:%M:%S')

        if now != end_time_string:
            time_left = end_time - datetime.today()
            time_left_string = str(time_left).split(':')
            remaining_time = f'REMAINING: {time_left_string[0]}:{time_left_string[1]}:{time_left_string[2][0:2]}'
            print(f'    {remaining_time}    '.center(100, '*'), end='\r')

        else:
            print('    TIMES UP!!    '.center(100, '*'))
            print()
            break


if __name__ == '__main__':

    display_menu()

    while True:

        selection = input("CHOICE: ")

        if selection.lower() == 'q':
            print("Goodbye")
            break
        elif selection.lower() == 'm':
            display_menu()
        elif selection == '1':
            while True:
                print()
                print(f'The current timeout is set to {timeout_time}')
                sel = input("ENTER Time in Minutes, (m)enu: ")
                if sel == 'm':
                    display_menu()
                    break
                elif sel.isdecimal():
                    timeout_time = timedelta(minutes=int(sel))
                    display_menu()
                    break
                else:
                    print('Invalid Option!')

        elif selection == '2':
            countdown()
