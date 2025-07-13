# Hangman Game
import random

words = ['python', 'internship', 'codealpha', 'programming']
word = random.choice(words)
guesses = ''
turns = 6

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    print()

    if failed == 0:
        print("You Win!")
        print("The word is:", word)
        break

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print(f"You have {turns} more guesses")

        if turns == 0:
            print("You Lose! The word was:", word)
