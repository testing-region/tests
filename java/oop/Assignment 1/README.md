# Assignment Description

In this assignment, you will write a computer version of a game called the “Stones Game”. In this game, two players take turns picking stones from an initial pile of stones (the starting number of stones must be odd), until there are no stones left. The player who ends up with an odd number of stones wins. You can play this game with a friend and a physical pile of stones to make sure you understand the game.

For example:

Suppose we start out with 99 stones. Let’s say the players’ moves are as follows:

1. Player 1 picks 23 stones. There are 76 stones left.
2. Player 2 picks 17 stones. There are 59 stones left.
3. Player 1 picks 20 stones and now has 43 stones in total. There are 39 stones left
4. Player 2 picks 24 stones and now has 41 stones in total. There are 15 stones left
5. Player 1 picks 14 stones and now has 57 stones in total. There is 1 stone left
6. Player 2 picks 1 stone and now has 42 stones in total. There are 0 stones left.

In this game, Player 1 wins because he/she ends up with an odd number of stones.

This is how your computer version of the game will work:

- The game starts by asking the users to enter the starting number of stones.
- The number entered must be positive and odd.
- If they don’t enter a positive odd number, keep prompting them until they do.
- Next, ask for the names of the two players so that you can refer to them by name.
- Next, in each round of the game, ask the players in turn to enter the number of stones to pick. Check that they enter a valid amount. If they enter an invalid amount (more details below), keep prompting them to re-enter information until they enter a valid amount. Once they have entered a valid amount, update the number of stones the player has, as well as the number of stones left. After each move, display a summary of the number of stones the player has, and how many stones are left.
- When there are no more stones left, the game ends, and the winner is announced.

There are some rules about how many stones a player is allowed to pick up in a given turn:

- A player must pick at least 1 stone (they cannot pick 0 stones)
- The first player to make a move cannot pick more than half of the initial number of stones (i.e. if we start out with 99 stones, the first player to take a turn may pick any number between 1 and 49).
- On subsequent plays, a player is not allowed to pick more than 2 times the number picked by the other user in their last turn, and may also not pick more stones than are available.

Below is an excerpt of a partial run from my Game of Stones. The beginning and end of the program is not shown:

---

Ayorkor (Player 1) has 0 stones.

Kofi (Player 2) has 0 stones.

There are 99 stones left in the pile

Ayorkor, choose between 1 and 49 stones

49

Ayorkor (Player 1) has 49 stones.

Kofi (Player 2) has 0 stones.

There are 50 stones left in the pile

Kofi, choose between 1 and 50 stones

3

Ayorkor (Player 1) has 49 stones.

Kofi (Player 2) has 3 stones.

There are 47 stones left in the pile

Ayorkor, choose between 1 and 6 stones

6

Ayorkor (Player 1) has 55 stones.

Kofi (Player 2) has 3 stones.

There are 41 stones left in the pile

Kofi, choose between 1 and 12 stones

---

Tasks:

- You are required to design an algorithm for the above task, before you start the implementation. Please show your algorithm to the instructor or FI for feedback, no later than Tuesday.

- Write your program. You may find it helpful to find write a basic version of the program before you add code for error-checking and asking the user to re-enter valid information where necessary.

- Test your programme thoroughly and submit a Word or a text document showing output from at least one test run of your program. Choose your test input carefully, to demonstrate the functionality of your program, including the error-catching functionality. The quality of your testing also factors into the grade for the assignment.
