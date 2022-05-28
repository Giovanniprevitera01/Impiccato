import random

words = []
with open('wordlist.txt') as f:
    for line in f:
        words.append(line.strip())

word = random.choice(words)
print(word)