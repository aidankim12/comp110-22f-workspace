"""EX01 - Chardle (my first steps towards Wordle. Finds the instances of a character in a five letter word."""

_author_ = "730535846"

word: str = input("Enter a 5 character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters.")
    exit() 
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Charcter must be a single character.")
    exit()
counter: int = 0
print("Searching for " + character + " in " + word)
if word[0] == character:
    print(character + " found at index 0")
    counter = counter + 1
if word[1] == character:
    print(character + " found at index 1")
    counter = counter + 1
if word[2] == character:
    print(character + " found at index 2")
    counter = counter + 1
if word[3] == character:
    print(character + " found at index 3")
    counter = counter + 1
if word[4] == character:
    print(character + " found at index 4")
    counter = counter + 1

if counter > 0:
    print(str(counter) + " instances of " + character + " found in " + word)
else:
    print("No instances of " + character + " found in " + word)
