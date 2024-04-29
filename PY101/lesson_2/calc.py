import math
import json
import os

language = ['en', 'tm', 'hi']
RE_RUN = 'y'

# Opening the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    data = json.load(file) # 'data' contains the contents of the JSON file

def message(prompt):
    # Printing the messages
    print("==> " + prompt)

def invalid_number(number):
    # Logic for finding whether a number is valid
    try:
        float(number)
        return check_invalid_numerical(number)
    except ValueError:
        return True

def check_invalid_numerical(number):
    # Check of invalid numerical inputs such as NaN or inf
    if math.isnan(float(number)) or math.isinf(float(number)):
        return True
    return False

def calculate(oprn, no1, no2, langs):
    # Defining function for calculator operations
    try:
        match oprn:
            case "1":
                answer = round((float(no1) + float(no2)), 2)
                op_name = "addition"
            case "2":
                answer = round((float(no1) - float(no2)), 2)
                op_name = "subtraction"
            case "3":
                answer = round((float(no1) * float(no2)), 2)
                op_name = "multiplication"
            case "4":
                if float(no2) == 0:
                    raise ZeroDivisionError
                answer = round((float(no1) / float(no2)), 2)
                op_name = "division"

    except ZeroDivisionError:
        return message(data[langs]["zero_division_error"])

    output = data[langs]['output_ans'].format(op_name=op_name, answer=answer)
    return message(output)

def clear_screen():
    # Clearing the screen
    if os.name == 'nt':
        os.system('cls') # For windows
    else:
        os.system('clear') # For mac OS & Unix

# Calculator begins
while RE_RUN not in ['n', 'no', 'nah'] or RE_RUN in ['yes', 'y', 'yeah']:

    message("Supported languages for the calculator:\n"
            "'en' for English\n"
            "'tm' for Tamil\n"
            "'hi' for Hindi\n"
            "Choose your preferred language: ")
    lang = input()

    while lang not in language:
        message("Invalid selection. Select from 'en', 'tm', 'hi'")
        lang = input()

    message(data[lang]["welcome"]) # Welcome message

    message(data[lang]["input_first_number"])
    number1 = input()

    # Checks if the input is valid otherwise prompts for a new input
    while invalid_number(number1):
        message(data[lang]["invalid_number1"])
        number1 = input()

    message(data[lang]["input_second_number"])
    number2 = input()

    # Checks if the input is valid otherwise prompts for a new input
    while invalid_number(number2):
        message(data[lang]["invalid_number2"])
        number2 = input()

    # Asking the user for what operation they would like to perform

    message(data[lang]["valid_operations"])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        message(data[lang]["invalid_operation"])
        operation = input()

    calculate(operation, number1, number2, lang) # Call calc fn.

# Asking if the user needs to use the calculator again
    message(data[lang]["calculate_again"])
    RE_RUN = input().lower()
    while RE_RUN not in ['n', 'no', 'nah', 'yes', 'y', 'yeah']:
        message(data[lang]["invalid_re_run_input"])
        RE_RUN = input().lower()

    clear_screen() # Clears the terminal screen for new calculation

    if RE_RUN in ['n', 'no', 'nah']:
        message(data[lang]["thank_you"])