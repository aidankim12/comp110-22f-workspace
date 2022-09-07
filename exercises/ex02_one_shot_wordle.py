"""A one-guess wordle program."""

__author__ = "730535846"

secret_word: str = "python"
question: str = input("What is your 6-letter guess? ")
counter: int = 0
counter_2: int = 0
WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
checker: str = ""

if len(question) != 6:
    question = input("That was not 6 letters! Try again: ")

while counter < len(secret_word):
    if  secret_word[counter] == question[counter]:
        checker += GREEN_BOX
        counter += 1
    elif secret_word[counter] != question[counter]:
        while counter_2 < len(secret_word):
            if question[counter] == secret_word[counter_2] and counter != counter_2:
                checker += YELLOW_BOX
                counter_2 += 1
            else:
                counter_2 += 1
        counter_2 = 0
        if len(checker) == counter: 
            checker += WHITE_BOX
            counter += 1
        else:
            counter += 1


print(checker)
if secret_word == question:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")