"""
Title          : Math Problem Generator
Author         : Yasharth Bajpai
Created        : 10th DEC 2024
Last Modified  : 14th JAN 2025
Version        : 1.0

Description    : This script generates and presents a series of math problems to the user.
                 It adapts the difficulty based on user input and tracks performance metrics
                 such as time taken and accuracy.

Dependencies   : 
    - Python 3.x
    - random module
    - time module

Usage          : Run the script and enter the desired difficulty level when prompted.
                 Solve the generated math problems and receive performance feedback at the end.

Notes          : The script generates problems using addition, subtraction, and multiplication.
                 The difficulty increases progressively as the user solves problems correctly.

License        : Creative Commons Zero v1.0 Universal

"""


import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
while True:
    MAX_OPERAND = input("Enter the Level: ")
    if MAX_OPERAND.isdigit() :
        MAX_OPERAND = int(MAX_OPERAND) + 3
        break
    else:
        print("Please enter a valid number")

TOTAL_PROBLEMS = MAX_OPERAND - MIN_OPERAND + 1

def generate_problem(min_operand):
    left = random.randint(min_operand, MAX_OPERAND)
    right = random.randint(min_operand, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

current_min_operand = MIN_OPERAND
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem(current_min_operand)
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
    

    if current_min_operand < MAX_OPERAND:
        current_min_operand += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
print("You got", wrong, "wrong answers.")
print("Your score is", TOTAL_PROBLEMS - wrong, "out of", TOTAL_PROBLEMS)
print("Your percentage is ", round((TOTAL_PROBLEMS - wrong) / TOTAL_PROBLEMS * 100, 2), "%")
print("----------------------")