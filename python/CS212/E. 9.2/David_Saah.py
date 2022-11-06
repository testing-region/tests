import time

# Store the wordlist in a variable
with open("words.txt") as file:
    words = [line.strip() for line in file.readlines()]

################
# Q 9.1
################

# label output
print("Ex. 9.1")
print("-" * 50)

print("The words greater than 20 are:")

# loop through the list to print words greater than 20
for word in words:
    if len(word) > 20:
        print(word)

time.sleep(2)
################
# Q 9.2
################

# label output
print("")
print("Ex. 9.2")
print("-" * 50)


def has_no_e(word):
    """checks if a word has 'e'

    Args:
        word (str): word to be checked

    Returns:
        bool: whether 'e' exists
    """
    return not ("e" in word)


print("The list of words with no 'e' are:")

num_e = 0
# display words that have no 'e'
for word in words:
    if has_no_e(word):
        num_e += 1
        print(word)

no_e_percent = (num_e / len(words)) * 100
print("")
print("The percentage of words with no 'e' is", round(no_e_percent, 2), "%")

time.sleep(2)
################
# Q 9.3
################

# label output
print("")
print("Ex. 9.3")
print("-" * 50)


def avoids(word, forbidden_word):
    """Returns true if the word does not use any of the forbidden letters

    Args:
        word (str): word to be checked
        forbidden_word (str): the letters that must not be present in the word

    Returns:
        bool: whether the word has any if the forbidden letters
    """
    for letter in forbidden_word:
        if letter in word:
            return False

    return True


forbidden_word = input("Enter a string of forbidden letters: ")
forbidden_word_count = 0

# print words that do not use any forbidden characters
for word in words:
    if avoids(word, forbidden_word):
        forbidden_word_count += 1

print(forbidden_word_count, "words do not have the forbidden letters")

time.sleep(2)
################
# Q 9.4
################

# label output
print("")
print("Ex. 9.4")
print("-" * 50)


def uses_only(word, characters):
    """Return True if `word` contains only all the letters in `characters`

    Args:
        word (str): word to be checked
        characters (str): the list of letters `word` must contain

    Returns:
        _type_: _description_
    """
    if len(characters) != len(word):
        return False

    for letter in characters:
        if not (letter in word):
            return False

    return True


characters = input("Enter a string of characters: ")
num_words = 0

for word in words:
    if uses_only(word, characters):
        num_words += 1

print(num_words, "word(s) uses only '", characters, "'")

time.sleep(2)
################
# Q 9.5
################

# label output
print("")
print("Ex. 9.5")
print("-" * 50)


def uses_all(word, letters):
    """Return True if `word` uses all the letters specified

    Args:
        word (str): word to be checks
        letters (str): required letters for the word to have.

    Returns:
        bool: whether all the letters are present in the word or not
    """
    for letter in letters:
        if not (letter in word):
            return False

    return True


num_aeiou = 0
num_aeiouy = 0

for word in words:
    if uses_all(word, "aeiou"):
        num_aeiou += 1

    if uses_all(word, "aeiouy"):
        num_aeiouy += 1

print("The number of words that use 'aeiou' are", num_aeiou)
print("The number of words that use 'aeiouy' are", num_aeiouy)

time.sleep(5)
################
# Q 9.6
################

# label output
print("")
print("Ex. 9.6")
print("-" * 50)


def is_abecedarian(word):
    """checks if all the letters in a word appears in alphabetical order

    Args:
        word (str): word to be check

    Returns:
        bool: whether the word is in alphabetical order or not
    """
    # convert the word to all lowercase to handle semantic errors
    word = word.lower()

    # loop through letters and compare if they come one after the other
    # comparing strings compares their binary equivalent
    for index in range(1, len(word)):
        initial = word[index - 1]
        next = word[index]
        if initial > next:
            return False

    return True


num_abecedarian = 0
for word in words:
    if is_abecedarian(word):
        num_abecedarian += 1

print(num_abecedarian, "words have their letters in alphabetical order")
