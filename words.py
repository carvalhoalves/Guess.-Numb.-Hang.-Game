from constants import WRITE, NO, READ, REMOVE, STOP, INF
from clear import clear_screen


def analyze_input(string, variable, lower_limit=-INF(), upper_limit=INF()):
    while True:
        if string.isnumeric():
            if int(string) < lower_limit or int(string) > upper_limit:
                if variable == 'operation':
                    print('\n\nYou have entered an invalid operation.')
                else:
                    print('\n\nYou have entered an invalid option.')
            else:
                break
        else:
            print('\n\nYou have entered an invalid sequence of characters.')

        if variable == 'operation':
            string = input('\nPlease, type in a number that represents one of the five possible operations that were '
                           'presented to you and then press ENTER.\n> ')
        else:
            string = input('\nPlease, type in a number that represents one of the two possible choices that were '
                           'presented to you and then press ENTER.\n> ')

    return int(string)


def empty():
    return len(read_lines()) == 0


def execute(operation):
    if operation == WRITE():
        print('\n\nYou have chosen to write in your text file.')

        word = input('\nTo do that, type in a word of your choice and press ENTER.\n> ')
        word = word.strip().upper()

        words = read_lines()

        if word not in words:
            write(word)
            print(f'\n\nThe word {word} was successfully written in your text file!')
        else:
            print(f"\n\nThe word {word} it's already in your text file."
                  f"\n\nPlease, type in a different word next time.")
    else:
        if operation == READ():
            print('\n\nYou have chosen to read your text file.')

            written_words = len(read_lines())

            if written_words > 0:  # IF THE FILE CONTAINS AT LEAST 1 WRITTEN WORD ON IT, THEN
                if written_words > 1:
                    print(f'\nAt the moment, it contains {written_words} words.')
                else:
                    print('\nAt the moment, it contains only one word.')

                print('\nwords.txt')

                print('\n', read('words.txt'), end='', sep='')
            else:
                print("\nAt the moment, it's empty.")
        else:
            if operation == REMOVE():
                print('\n\nYou have chosen to remove a word from your text file.')

                word = input('\nTo do that, type in the word that you want to remove and press ENTER.\n> ')
                word = word.strip().upper()

                words = read_lines()

                if word in words:
                    remove(word, words)
                    print(f'\n\nThe word {word} was successfully removed from your text file.')
                else:
                    print(f"\n\nThe word {word} couldn't be removed. Your text file doesn't contain this word.")
            else:
                print('\n\nYou have chosen to seek a word in your text file.')

                word = input('\nTo do that, type in the word that you want to seek and press ENTER.\n> ')
                word = word.strip().upper()

                words = read_lines()

                if word in words:
                    print(f'\n\nThe word {word} was found in your text file!')
                else:
                    print(f"\n\nThe word {word} was not found. Your text file doesn't contain this word.")


def manager():
    print("\n\nIt's important to know (or remember, if this is not your first time here) that all words in this game "
          "are stored in a text file."
          "\n\nThat being said, you must know (or might remember) that you will be able to use a few operations to "
          "alter this file."
          "\n\nFeel free to add – write – or remove words as much as you want.")

    print('\n\nBelow, you can see the four operations that you could use to manage the I/O of your text file.'
          '\n\nYou can also see a fifth operation, but you must choose this option only if you decide to stop the '
          'management of your text file at a certain moment.')

    while True:
        print('\n\nWhich operation would you like to use?'
              '\n\n1. Write Word     2. Read File     3. Remove Word     4. Seek Word     5. Stop Management')

        operation = input('\nType in the number that represents the operation chosen by you and press ENTER.\n> ')

        operation = analyze_input(operation, 'operation', lower_limit=1, upper_limit=5)

        clear_screen()

        if operation != STOP():
            execute(operation)
        else:
            if not empty():
                print("\n\nYou have decided to stop the management of your text file."
                      "\n\nThe Hangman Game is ready for you to play and it's about to start! :)")
                break
            else:
                print("\n\nYou cannot stop the management of your text file while it's empty."
                      "\n\nPlease, write at least one word in your text file before you decide to stop "
                      "this management.")
                continue

        print('\n\nWould you like to continue managing your text file?'
              '\n\n1. Yes     2. No')

        option = input('\nType in the number that represents the option chosen by you and press ENTER.\n> ')

        option = analyze_input(option, 'option', lower_limit=1, upper_limit=2)

        clear_screen()

        if option == NO():
            if not empty():
                print("\n\nYou have decided to stop the management of your text file."
                      "\n\nThe Hangman Game is ready for you to play and it's about to start! :)")
                break
            else:
                print("\n\nYou cannot stop the management of your text file while it's empty."
                      "\n\nPlease, write at least one word in your text file before you decide to stop "
                      "this management.")
        else:
            print('\n\nYou have chosen to continue managing your text file.')


def read(words):
    with open(words, 'r') as File:
        return File.read()


def read_lines():
    with open('words.txt', 'r') as File:
        return [string.strip() for string in File.readlines()]


def remove(string, lines):
    with open('words.txt', 'w') as File:
        for line in lines:
            if line != string:
                File.write(line + '\n')


def write(string):
    with open('words.txt', 'a') as File:
        File.write(string + '\n')
