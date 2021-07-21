user_pass = input("Enter your password: ")

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '`', '~', '#', '-', '$', '_', '%', '=', '^', '+', '&', '{', '*', '}', '(', '[', ']', ')', ',', '.', '/', ';', '<', '>', ':', '?', '|', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]

guess = ""

lenpass = len(user_pass)

for x in user_pass:
	for y in password:
		if x == y:
			guess += y
		else:
			continue
print('\n')
print("Your password is",guess)