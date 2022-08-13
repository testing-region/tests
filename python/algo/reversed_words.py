word = input("Enter a word: ")

word_stack = list(word)
reversed_word = []

for x in range(len(word_stack)):
    reversed_word.append(word_stack.pop())

print("Reversed word:", ''.join(reversed_word))
