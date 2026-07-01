
import random

print("welcome to hangman game!")

word_list=["apple","banana","orange","kiwi","mango","pineapple","papaya","watermelon","grapes"]
choosen_word=random.choice(word_list)

display=[]
for letter in choosen_word:
    display.append("_")
print(display)

lives = 6

while lives > 0 and "_" in display:

    guess_letter = input("Enter a letter: ")

    found = False

    for position in range(len(choosen_word)):
        letter = choosen_word[position]

        if guess_letter == letter:
            display[position] = guess_letter
            found = True

    if not found:
        lives -= 1
        print("Wrong guess!")
        print("Lives left:", lives)

    print(display)
print("you win the game!")


