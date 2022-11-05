def is_vowel(character):
    """checks if a character is a vowel

    Args:
        character (str): a character

    Returns:
        bool: vowel state of character
    """
    vowels = "aeiou"
    return character.lower() in vowels