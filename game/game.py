import random

words = []
with open('wordlist.txt') as f:
    for line in f:
        words.append(line.strip())

word = random.choice(words)
#print(word)

def wordGuessed(letter_list):
    print(' '.join(letter for letter in letter_list))

letters_guessed = []
for letter in word:
    letters_guessed.append('_')
print(letters_guessed)

while True:
    choise = input('Guess a letter --> ')
    if choise in word:
        for i, letter in enumerate(word):
            if letter == choise:
                letters_guessed[i] = choise
    else:
        print('Wrong!')

    print(letters_guessed)
    
    wordGuessed(letters_guessed)
