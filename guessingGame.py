# ------------------------------------------------------------
# Name: Donavan McFadden
# Student ID: Donmcf8357
# Date: October 27, 2026
# Course: SDC205 Python for Data Analytics
# Assignment: 2.7 Performance Assessment - Decisions, Loops,
#             Processing, Output Formatting
# Description: This program asks for the user's name and
# Student ID and greets them. The user then guesses a secret
# number between 1 and 10. An if/elif/else statement says if
# each guess is too high, too low, or correct, and the program
# counts how many tries it took. Finally, a while loop and a
# for loop each add 1 to the correct guess five times and show
# the results.
# ------------------------------------------------------------

print("Student ID: Donmcf8357")
print("=" * 45)

# Get the user's name and Student ID, then greet them
userName = input("Please enter your name: ")
studentId = input("Please enter your Student ID: ")
print()
print(f"Hello, {userName}! Welcome to the Number Guessing Game.")
print(f"Student ID: {studentId}")
print("=" * 45)

# The pre-determined number the user is trying to guess
secretNumber = 5
numberOfTries = 0
guessedCorrectly = False

# Keep asking until the user guesses the secret number
while not guessedCorrectly:
    userGuess = input("Enter a number between 1 and 10: ")

    # Make sure the guess is a whole number from 1 to 10
    if not userGuess.isdigit() or int(userGuess) < 1 or int(userGuess) > 10:
        print("That is not a whole number between 1 and 10. Please try again.")
        continue

    userGuess = int(userGuess)
    numberOfTries = numberOfTries + 1

    if userGuess > secretNumber:
        print(f"{userGuess} is too high. Try again.")
    elif userGuess < secretNumber:
        print(f"{userGuess} is too low. Try again.")
    else:
        print(f"{userGuess} is correct! You guessed the number.")
        guessedCorrectly = True

if numberOfTries == 1:
    print("It took you 1 try to guess correctly.")
else:
    print(f"It took you {numberOfTries} tries to guess correctly.")
print("=" * 45)

# While loop: add 1 to the correct guess five times
print("Output from the 'while' loop:")
whileValue = secretNumber
whileCounter = 0
while whileCounter < 5:
    newValue = whileValue + 1
    print(f"  Iteration {whileCounter + 1}: {whileValue} incremented by 1 is {newValue}")
    whileValue = newValue
    whileCounter = whileCounter + 1

print()

# For loop: does the same thing as the while loop
print("Output from the 'for' loop:")
forValue = secretNumber
for forCounter in range(5):
    newValue = forValue + 1
    print(f"  Iteration {forCounter + 1}: {forValue} incremented by 1 is {newValue}")
    forValue = newValue

print("=" * 45)
print(f"Thanks for playing, {userName}! (Student ID: Donmcf8357)")
