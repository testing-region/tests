# Lab 2

## Question 1

- [x] Create a Person class that has three instance variables:

  - [x] One for the person’s name.
  - [x] One for the person’s age.
  - [x] Third for the person’s gender.

- [x] Include accessor methods and mutator methods for each instance variable.
- [x] Create `setPerson` method that takes three arguments: name, age and gender of a person.

  - The program should **exit** if the caller tries to:
    - [x] Set a negative age for a Person.
    - [x] Set an invalid value for the gender.

## Question 2

- [x] Create a class that can be used to get acceptable integer from the user.
- [x] The class should have the following attributes:

    - [x] Minimum accepted value.
    - [x] Maximum accepted value.
    - [x] Prompt string.

- [x] Add `setInputParameters` method to take 3 arguments in order to set the three instance variables representing the minimum accepted value, maximum accepted value, and prompt string.
- [x] Add `getValue` method which displays the `prompt` and checks if the value read is within the allowed range.

    - [x] Keep asking for input until the user enters a valid value.
    - [x] Display an error message for each wrong value entered.
    - [x] The method returns the value read.

