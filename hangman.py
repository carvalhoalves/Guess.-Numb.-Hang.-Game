from constants import YES, INF
from clear import clear_screen
from random import randint
from words import manager, read_lines


def analyze_input(string, lower_limit=-INF(), upper_limit=INF()):
    while True:
        if string.isnumeric():
            if int(string) < lower_limit or int(string) > upper_limit:
                print('\n\nYou have entered an invalid option.')
            else:
                break
        else:
            print('\n\nYou have entered an invalid sequence of characters.')

        string = input('\nPlease, type in a number that represents one of the two possible choices that were presented '
                       'to you and then press ENTER.\n> ')

    return int(string)


def play():
    print('\n\nYou have chosen to play the Hangman Game.')

    lines = read_lines()
    #
    # 'lines' is a list that contains (or not, it could be empty) all the words written in the file 'words.txt'.

    list_length = len(lines)

    if list_length > 0:  # IF THE GAME (OR THE FILE) CONTAINS ONE OR MORE WORDS, THEN
        if list_length > 1:
            print(f'\n\nAt the moment, your game has {list_length} words to be discovered.')
        else:
            print('\n\nAt the moment, your game has only one word to be discovered.')

        print('\n\nWould you like to add some new words to the game?'
              '\n\n1. Yes     2. No')

        option = input('\nType in the number that represents the option chosen by you and press ENTER.\n> ')

        option = analyze_input(option, lower_limit=1, upper_limit=2)

        clear_screen()

        if option == YES():
            print("\n\nAs you wish! Let's add some new words before we play! :)")
            manager()
            #
            # 'manager()' is a function that is responsible for the management of the text file 'words.txt', wich is
            # the providing source of words to the Hangman Game. Through this function, the user will be able to write,
            # read, remove or seek a word in 'words.txt'.
    else:
        print('\n\nAt the moment, your game has no words to be discovered.')
        manager()
        #
        # This case is very specific, but if the file 'words.txt' has no words written on it, the user will be forced
        # to write at least one word in the file to be able to play the game.

    correct, hanged, hits, limit, mistakes, string = False, False, 0, 6, 0, list()

    lines = read_lines()
    #
    # The lines of 'words.txt' has to be read again, because the file may have been altered. Words could have been
    # written or removed from the file, so this operation or atribution is mandatory to secure that the game will
    # function correctly.

    word = lines[randint(0, len(lines) - 1)]
    #
    # Before the game starts, a word contained in 'words.txt' is randomly selected throgh the use of the imported
    # function 'randint()'.

    word_length = len(word)

    print("\n\nBefore the game really starts, it's important to know (or remember) that you can only commit 5 mistakes."
          "\n\nThe game will end when you miss your guess for the 6th time.")

    print("\n\nNow that you know this, we can finally start the game."
          "\n\nI'll give you a simple tip.")

    print(f'\n\nTHE WORD IS COMPOSED BY {word_length} LETTERS.')

    print('\n\nW O R D  :', end='')

    for index in range(word_length):
        string.append('__')
        print(' ', string[index], end='')

    print('\n', end='')

    while not correct and not hanged:
        letter = input('\nTo make your guess, type in a letter of your choice and press ENTER.\n> ')
        letter = letter.strip().upper()

        if letter in word:
            if letter not in string:
                occurrences = int()

                for index in range(word_length):
                    if letter == word[index]:
                        string[index] = word[index]
                        hits += 1
                        occurrences += 1

                if hits < word_length:
                    print('\n\nYou have guessed correctly!')

                    if occurrences > 1:
                        print(f'\nThere are {occurrences} occurrences of the letter {letter} in this word.')
                    else:
                        print(f'\nThere is only one occurrence of the letter {letter} in this word.')
                else:
                    print(f'\n\nYou have guessed correctly and the word is complete!\n\n'
                          f'The last missing letter was exactly the letter {letter}!\n\n'
                          f'Congrats! :)')
                    correct = True
            else:
                print(f'\n\nThe letter {letter} was already discovered by you.'
                      f'\n\nPlease, type in different letters.')
        else:
            mistakes += 1

            if mistakes < limit:
                print('\n\nYou have guessed incorrectly.')

                if mistakes < 4:
                    if mistakes == 1:
                        print('\nThis is your 1st mistake.', end=' ')
                    else:
                        if mistakes == 2:
                            print('\nThis is your 2nd mistake.', end=' ')
                        else:
                            print('\nThis is your 3rd mistake.', end=' ')

                    print(f'You can still make {5 - mistakes} more mistakes before the game ends.')
                else:
                    print(f'\nThis is your {mistakes}th mistake.', end=' ')

                    if mistakes == 4:
                        print('You can still make one more mistake before the game ends.')
                    else:
                        print('The game will end if you miss your next guess.')
            else:
                print("\n\nYou were hanged. :("
                      "\n\nBut don't be sad about it, I'm sure you will do better next time. :)")

        if mistakes < limit:
            print('\n\nW O R D  :', end='')

            for character in string:
                print(' ', character, end='')

            print('\n', end='')
        else:
            hanged = True
