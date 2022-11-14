#############
# Ex. 8.2
#############
print("Ex. 8.2")
print("-"*30)

print("The number of a's in banana are", "banana".count("a"))


#############
# Ex. 8.3
#############
print("\nEx. 8.3")
print("-"*30)

print("redivider" == "redivider"[::-1])


#############
# Ex. 8.4
#############
"""
# any_lowercase1
It checks all the letters in variable `s` and returns `True` when it finds the first lowercase character in the string.

# any_lowercase2
It has an iteration of all the letters in variable `s`. The condition uses a string "c" instead of the variable, `c`. As a result, it will always return the string, "True".

# any_lowercase3
It iterates through the letters in variable `s` and assigns the state of the character to a variable called `flag`. If all the letters are lowercase, the function returns `True`. However, if uppercase letters are in-between the string, the function would still return `True` because `flag` holds the last value of `c.islower()`.

# any_lowercase4
It begins by assigning `False` to variable `flag`. It iterates through all the characters in the string and `flag` is assigned to the output of the expression, `flag or c.islower()`. This function would return `True` if at least one lowercase letter is present in the string.

# any_lowercase5
The last function iterates through all the letters in the string and checks if they are all lowercase, else it returns `False`.
"""


#############
# Ex. 8.5
#############
print("\nEx. 8.5")
print("-"*30)

def rotate_word(word, shift):
    new_word = ""
    
    for letter in word:
        new_word += chr(ord(letter) + shift)
    
    return new_word

print("abcde with shift=1:", rotate_word("abcde", 1))
print("abcde with shift=5:", rotate_word("programming", 5))