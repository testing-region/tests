def first(word): 
    return word[0] 
 
def last(word): 
    return word[-1] 
 
def middle(word): 
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
    
    if first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))


# Tests
word1 = "noon"
word2 = "redivider"
word3 = "food"
word4 = "hospital"

print("Checking if the following words are palidromes")
print(word1, ":", is_palindrome(word1))
print(word2, ":", is_palindrome(word2))
print(word3, ":", is_palindrome(word3))
print(word4, ":", is_palindrome(word4))
