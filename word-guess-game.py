import random

def WordGuessingGame():
    with open('words_alpha.txt', 'r') as file:
        alltext = file.read()
        random_words = list(map(str, alltext.split()))


    word = random.choice(random_words)    
    starting_word = list(word)
    wins = 0
    losses = 0
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
                if turns == 0:
                    print('Sorry! You have no guesses left! Your game is over')
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
                    turns -= 1
                    print('Sorry! That guess is wrong! Try again!')
                    print('You have', turns - 1, 'guesses left.')
    if turns == 0:
        losses += 1
        playAgain = input('Would you like to play again? (Yes or No): ')
        if playAgain == 'Yes':
            WordGuessingGame()
        if playAgain == 'No':
            exit
        else:
            wins += 1


WordGuessingGame()
