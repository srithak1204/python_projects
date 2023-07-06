#import
import random

print("Let's play HangMan!!")
print("Guess the word, you have only six lifes")
words = ["apple","aeroplane","satisfaction","beautiful","spacecraft"]
r= random.choice(words)
word = list(r)
show_word=[]
for i in range(0,len(word)):
    show_word.append('_')
print(show_word)
deside = False
deside2 = False
p = 0
while p != 6:
    guess = input("guess a letter: ")
    pre = False

    for k in range(len(word)):
        if word[k] == guess:
            show_word[k] = guess
            pre = True
    count = 0
    for k in show_word:
        if k == '_':
            count += 1
    if count == 0:
        print(show_word)
        print("you win")
        deside = True
        break

    if pre is True:
        print('you have guessed right')
        print(show_word)
        continue

    print('you have guessed wrong. you will loose one life')
    p += 1
    if p == 1:
        print("""
              ________
                 |   |
                 0   |
                     |
                     |
            """)
    elif p == 2:
        print(
                """
                ________
                   |   |
                   0   |
                   |   |
                       |
                """)
    elif p == 3:
        print("""
                ________
                   |   |
                   0   |
                  /|   |
                       |
                """)
    elif p == 4:
        print("""
                ________
                   |   |
                   0   |
                  /|\  |
                       |
                """)
    elif p == 5:
        print(
                """
                ________
                   |   |
                   0   |
                  /|\  |
                  /    |
                """)
    elif p == 6:
        print(
                """
                ________
                   |   |
                   0   |
                  /|\  |
                  / \  |
                """)
        print("you loose\nyou lost all of your lives")
        deside2 = True



if deside is False and deside2 is False:
    print("you loose\nyou lost all of your lives")
