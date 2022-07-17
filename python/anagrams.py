# Word Jumble
# The player has to guess the original word
import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

HINTS = ("snake", "scrambled", "CMIS101", "CMIS210", "solution", "technology")

# create a jumbled version of the word


def createJumbled(word):
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    return jumble

# start the game


print("""
           Word Jumble!
   Unscramble the letters to make a word.
""")
helpcount = 0
totalGame = 0
playMore = 'yes'
while playMore == 'yes':
    # pick one word randomly from the sequence
    word = random.choice(WORDS)
    index = WORDS.index(word)
# create a variable to use later to see if the guess is correct
    correct = word
    jumble = createJumbled(word)
    print("The jumble is:", jumble)
    print("\nFor a hint, type in 'yes'. If not, type in 'no'.")
    help = input("Do you need a hint?: ")
    if help == "yes":
        hint = HINTS[index]  # getHint(word)
        print(hint)
        helpcount += 1
        guess = input("\nYour guess: ")
    elif help == "no":
        guess = input("\nYour guess: ")
    while guess != correct and guess != "":
        print("Sorry, that's not it.")
        print("\nFor a hint, type in 'yes'. If not, type in 'no'.")
        help = input("Do you need a hint?: ")
        if help == "yes":
            hint = HINTS[index]  # getHint(word)
            print(hint)
            helpcount += 1
        guess = input("Your guess: ")
    if guess == correct:
        print("That's it!  You guessed it!")
    if helpcount == 0:
        print("And you didn't even need a hint! You're awesome!\n")
    totalGame += 1
    print("\nTo continue game, type 'yes'.")
    playMore = input("Do you want to continue: ")
print('\n\n')
print('    Total games:\t', totalGame)
print('Sought for help:\t', helpcount)
print(' Final Score is:\t', totalGame-helpcount)
print("Thanks for playing.")
