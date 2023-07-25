from constants import GUESSING_NUMBERS, NO, INF
from clear import clear_screen
import guessing_numbers
import hangman


def analyze_input(string, variable, lower_limit=-INF(), upper_limit=INF()):
    while True:
        if string.isnumeric():
            if int(string) < lower_limit or int(string) > upper_limit:
                print('\n\nYou have entered an invalid option.')
            else:
                break
        else:
            print('\n\nYou have entered an invalid sequence of characters.')

        if variable == 'game':
            string = input('\nPlease, type in a number that represents one of the two possible games that you can play '
                           'and then press ENTER.\n> ')
        else:
            string = input('\nPlease, type in a number that represents one of the two possible choices that were '
                           'presented to you and then press ENTER.\n> ')

    return int(string)


if __name__ == '__main__':
    clear_screen()

    print("\n\nHello! It's nice to have you here! :)")

    while True:
        print('\n\nBelow, you can see the two games that you can play.'
              '\n\n1. Guessing Numbers     2. Hangman Game')

        game = input('\nTo play one of them, type in the number that represents the game chosen by you and press '
                     'ENTER.\n> ')
        game = analyze_input(game, 'game', lower_limit=1, upper_limit=2)

        clear_screen()

        if game == GUESSING_NUMBERS():
            guessing_numbers.play()
        else:
            hangman.play()

        print('\n\nWould you like to play more?'
              "\n\n1. Yes, I would like to play this or another game!     2. No, I want to stop playing.")

        option = input('\nType in the number that represents the option chosen by you and press ENTER.\n> ')

        option = analyze_input(option, 'option', lower_limit=1, upper_limit=2)

        clear_screen()

        if option == NO():
            print('\n\nI hope you have enjoyed the game!'
                  '\n\nSee you later! :)\n')
            break
        else:
            print("\n\nAlright! Let's play more! :)")
