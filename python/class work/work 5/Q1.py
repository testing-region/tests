"""
Create a function greet_user() that can tell the user Hello! and
also greet them by their name. Create a username that will allow
the function to accept any value of username specified. The function
will expect the user to provide a value for username each time you call it
"""

username = input("Enter your name: ")

def greet_user(username):
    """greet the user by their name"""
    return "Hello " + username + "!"

print(greet_user(username))