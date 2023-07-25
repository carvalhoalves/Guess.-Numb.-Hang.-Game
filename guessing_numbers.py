from constants import INF
from clear import clear_screen
from random import randint


def analyze_input(string, variable, lower_limit=-INF(), upper_limit=INF()):
    while True:
        if string.isnumeric():
            if int(string) < lower_limit or int(string) > upper_limit:
                if variable == 'guess':
                    print('\n\nYou have entered a number out of the range mentioned above.')
                else:
                    print('\n\nYou have entered an invalid level.')
            else:
                break
        else:
            print('\n\nYou have entered an invalid sequence of characters.')

        if variable == 'guess':
            string = input('\nPlease, type in an integer number between 1 and 100 and press ENTER.\n> ')
        else:
            string = input('\nPlease, type in a number that represents one of the three possible levels that were '
                           'presented to you and then press ENTER.\n> ')

    return int(string)


def play():
    attempts, points, secret_number = 0, 0, randint(1, 100)
    #
    # The 'secret_number' is a randomly selected number between 1 and 100. Its selection is made by the imported
    # function 'randint()'.

    print('\n\nYou have chosen to play the game Guessing Numbers.')

    print('\n\nTo start the game, choose one of the levels below.'
          '\n\n1. Easy     2. Medium     3. Hard')

    level = input('\nType in the number that represents the level chosen by you and press ENTER.\n> ')

    level = analyze_input(level, 'level', lower_limit=1, upper_limit=3)

    clear_screen()

    if level == 1:
        attempts, points = 20, 2000
        print('\n\nYou have chosen the level Easy.')
    else:
        if level == 2:
            attempts, points = 15, 1500
            print('\n\nYou have chosen the level Medium.')
        else:
            attempts, points = 10, 1000
            print('\n\nYou have chosen the level Hard.')

    print(f'\nYou will have {attempts} attempts to make your guesses about the secret number.')

    for attempt in range(1, attempts + 1):
        if attempt < 4:
            if attempt == 1:
                print('\n\nThis is your 1st attempt.', end=' ')
            else:
                if attempt == 2:
                    print('\n\nThis is your 2nd attempt.', end=' ')
                else:
                    print('\n\nThis is your 3rd attempt.', end=' ')
        else:
            print(f'\n\nThis is your {attempt}th attempt.', end=' ')

        if attempt > 1:
            print(f'Current Score: {points} Points')
        else:
            print(f'Initial Score: {points} Points')

        guess = input('\nType in an integer number between 1 and 100 and press ENTER.\n> ')

        guess = analyze_input(guess, 'guess', lower_limit=1, upper_limit=100)

        clear_screen()

        if guess == secret_number:
            print(f'\n\nYou have guessed correctly! Your guess was the number {guess} and the secret number is exactly '
                  f'{secret_number}!'
                  f'\n\nFinal Score: {points} Points'
                  f'\n\nWell done! :)')
            break
        else:
            print('\n\nYou have guessed incorrectly.')

            if guess > secret_number:
                print(f'\nThe number {guess} is bigger than the secret number.')
            else:
                print(f'\nThe number {guess} is smaller than the secret number.')

            points -= abs(secret_number - guess)

            if attempt == attempts:
                print(f'\n\nUnfortunately, all your guesses were wrong. :( The secret number was the number '
                      f'{secret_number}.'
                      f"\n\nBut don't worry, you will have better luck next time! :)"
                      f"\n\nFinal Score: {points} Points")
