word = 'mississippi'
starting_word = list(word)
turns = 7
guesses_list = []

while turns > 0:
    guess = str(input('Please make a guess: '))
    if len(guess) == 1:
        guesses_list.append(guess)
        if word.find(guess) == -1:
            print('Sorry that guess is not in the word. Try again.')
            print('You have', turns - 1, 'guesses left.')
            turns -= 1
            if turns == 0:
                print('Sorry! You have no guesses left! Your game is over')
        else:
            print('Nice! That guess is correct')
            print('You have', turns - 1, 'guesses left.')
            turns -= 1
            display = ''
            for letter in starting_word:
                    if letter in guesses_list:
                        display += letter
                    else:
                        display += ' _ '
            print(str(display))
            if display == word:
                print('Congratulations! You won!')
                print('The word is: ', word)
                break

    else:
        if len(guess) > 1:

            if guess == word:
                print('Congratulations! You won!')
                print('The word is: ', word)

            elif guess != word and turns == 1:
                print('Sorry! You are out of turns! Game over!')

            else:
                turns = turns - 1
                print('Sorry! That guess is wrong! Try again!')
                print('You have', turns - 1, 'guesses left.')
