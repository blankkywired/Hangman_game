import words
import hangdraw
import random



print('Welcome do Hangman Game Python')
print(hangdraw.hangman[6])

choosen_word = random.choice(words.animals)
choosen_word = choosen_word.lower()
placeholder = ""
for letter in choosen_word:
    placeholder += "_"
print(choosen_word)
print(f'Choosen Word: {placeholder}')


lifes = 6
correct_letters = []
index = 6

while lifes > 0:
    
    guess = input('Guess a letter in choosen word: ').lower()
    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    # print(hangdraw.hangman[index])
    # print('Progress:')
    # print(display)
    print(f'{hangdraw.hangman[index]}\nProgress:\n{display}')

    if not guess in choosen_word:
        lifes -= 1
        index -= 1
        print(hangdraw.hangman[index])
        if lifes == 0:
            print('You lose')
            break

    if not "_" in display:
        print('Great, you got it')
        print(f'The choosen word was {choosen_word}')
        break




