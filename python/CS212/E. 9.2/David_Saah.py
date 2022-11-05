################ 
### Q 9.1
################

# label output
print("Ex. 9.1")
print("-" * 50)

# Store the wordlist in words
with open("words.txt") as file:
    words = [line.strip() for line in file.readlines()]

"""
# loop through the list to print words greater than 20
for word in words:
    if len(word) > 20:
        print(word)

################
### Q 9.2
################

# label output
print("")
print("Ex. 9.2")
print("-" * 50)

def has_no_e(word):
    return not ("e" in word)

num_e = 0
# display words that have no 'e'
for word in words:
    if has_no_e(word):
        num_e += 1
        print(word)

no_e_percent = (num_e / len(words)) * 100
print("")
print("The percentage of words with no 'e' is", round(no_e_percent, 2), "%")

################
### Q 9.3
################

# label output
print("")
print("Ex. 9.3")
print("-" * 50)

def avoids(word, forbidden_word):
    for letter in forbidden_word:
        if letter in word:
            return False
    
    return True


forbidden_word = input("Enter a string of forbidden letters: ")

# print words that do not use any forbidden characters
for word in words:
    if avoids(word, forbidden_word):
        print(word)

################
### Q 9.4
################

# label output
print("")
print("Ex. 9.4")
print("-" * 50)

def uses_only(word, characters):
    if len(characters) != len(word):
        return False

    for letter in characters:
        if not (letter in word):
            return False
        
    return True

characters = input("Enter a string of characters: ")

for word in words:
    if uses_only(word, characters):
        print(word)

################
### Q 9.5
################

# label output
print("")
print("Ex. 9.5")
print("-" * 50)

def uses_all(word, letters):
    if len(letters) != len(word):
        return False

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

print("The number of words that use aeiou are", num_aeiou)
print("The number of words that use aeiouy are", num_aeiouy)
"""
################
### Q 9.6
################

# label output
print("")
print("Ex. 9.6")
print("-" * 50)

def is_abecedarian(word):
    start = ord(word[0])

    for letter in word:
        if ord(letter) == start:
            start += 1
            continue
        return False
    
    return True

for word in words:
    if is_abecedarian:
        print(word)