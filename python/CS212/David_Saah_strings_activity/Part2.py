import Part1


def first_vowel_index(word):
    """returns the index of the first vowel in the word

    Args:
        word (str): word to check

    Returns:
        number: index of first vowel
    """
    for letter in word:
        if Part1.is_vowel(letter):
            return word.index(letter)
    
    return -1