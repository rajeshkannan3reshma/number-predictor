
# I built a small Python program that checks if a number is even or odd, and it also gives a fun prediction like a fake ML model.
# I used simple functions and logic to show how data can be used for prediction, even at a basic level.

import random

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Ask user to enter a number
user_input = int(input("Enter a number: "))
result = check_even_odd(user_input)
print("This number is:", result)

# Fake ML-style random prediction for next number
prediction = random.choice(["Even", "Odd"])
print("My prediction for your next number is:", prediction)
