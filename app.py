import random
from wordList import wordlist
from hangman import HANGMANPICS

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Game setup
randomWord = random.choice(wordlist).lower()
temp = ['_'] * len(randomWord)
score = 0
guessed_letters = set()

# Start screen
print(f"{CYAN}{'='*40}")
print("      Welcome to HANGMAN!")
print(f"{'='*40}{RESET}")
print(f"{YELLOW}Try to guess the word. You have {7 - score} wrong attempts left.{RESET}")

while score < 7:
    if ''.join(temp) == randomWord:
        break

    print(f"\n{HANGMANPICS[score]}")
    print(' '.join(temp))
    print(f"{YELLOW}Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}{RESET}")
    print(f"{YELLOW}Attempts left: {7 - score}{RESET}")

    guess = input(f"{CYAN}Guess a letter: {RESET}").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print(f"{RED}Please enter a single valid letter!{RESET}")
        continue

    if guess in guessed_letters:
        print(f"{RED}You've already guessed '{guess}'! Try another letter.{RESET}")
        continue

    guessed_letters.add(guess)

    # Check if letter is in the word
    if guess in randomWord:
        for i in range(len(randomWord)):
            if randomWord[i] == guess:
                temp[i] = guess
        print(f"{GREEN}Good guess!{RESET}")
    else:
        score += 1
        print(f"{RED}Wrong guess!{RESET}")

# End screen
if ''.join(temp) == randomWord:
    print(f"\n{GREEN}🎉 Congratulations! You guessed the word: {randomWord.upper()}!{RESET}")
else:
    print(f"{RED}💀 Game over! The word was: {randomWord.upper()}.{RESET}")