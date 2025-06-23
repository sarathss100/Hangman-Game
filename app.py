import wordList;
import random;

randomWord = random.choice(wordList.wordlist)
score = 0

def guessWord():
    letter = input('Please Guess a letter : ').lower()
    return letter

temp = ['_'] * len(randomWord)
guess = ''

while ''.join(temp) != randomWord:
    guess = guessWord()
    flag = False
    for i in range(len(randomWord)):
        if guess == randomWord[i]:
            temp[i] = guess
            flag = True

    guess = ''
    if flag:
        score += 1
        flag = False
    else: 
        score -= 1

    print(''.join(temp))
    print(f'Your score ${score}')

print('You won')