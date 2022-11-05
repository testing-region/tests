import Part2


def english_to_piglatin(word):
    """convert English word to Pig Latin

    Args:
        word (str): English word

    Returns:
        str: Pig Latin translation
    """
    vowel_index = Part2.first_vowel_index(word)

    if vowel_index == 0:
        return word + "way"
    elif vowel_index > 0:
        return word[vowel_index:] + word[:vowel_index] + "ay"
    
    return "No pig latin translation available for words without vowels"
    