import words
import hangdraw
import random

print("""
                                         
  /\  /\__ _ _ __   __ _  /\/\   __ _ _ __   
 / /_/ / _` | '_ \ / _` |/    \ / _` | '_ \  
/ __  / (_| | | | | (_| / /\/\ \ (_| | | | | 
\/ /_/ \__,_|_| |_|\__, \/    \/\__,_|_| |_| 
                   |___/                     
""")

print('Welcome do Hangman Game Python')
print(hangdraw.hangman[6])

choosen_word = random.choice(words.animals)
choosen_word = choosen_word.lower()

placeholder = ""
for letter in choosen_word:
    placeholder += "_"
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




