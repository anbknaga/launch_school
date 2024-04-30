import math
import json
import os

RE_RUN = 'y'

# Opening the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    data = json.load(file) # 'data' contains the contents of the JSON file

def message(prompt):
    # Printing the messages
    print("==> " + prompt)

def display_language_choices(text):
    #Display available languages in the calculator
    language = ['en', 'tm', 'hi']
    message(f"{text}")
    langs = input().lower()

    while langs not in language:
        message("Invalid selection. Select from 'en', 'tm', 'hi'")
        langs = input().lower()

    return langs

def get_number(lang, number_text):
    # Prompting numbers for calculator oeprations
    message(data[lang][number_text])
    number = input()

    # Checks if the input is valid otherwise prompts for a new input
    while invalid_number(number):
        message(data[lang]["invalid_number"])
        number = input()

    return number

def prompt_operator(lang, prompt_text):
    # Defining function for prompting the operation value
    message(data[lang][prompt_text])
    ops = input()

    while ops not in ['1', '2', '3', '4']:
        message(data[lang]["invalid_operation"])
        ops = input()

    return ops

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

def calculate(operation, number1, number2):
    # Defining function for calculator operations
    try:
        match operation:
            case "1":
                answer = round((float(number1) + float(number2)), 2)
                op_name = "added with"
            case "2":
                answer = round((float(number1) - float(number2)), 2)
                op_name = "subtracted by"
            case "3":
                answer = round((float(number1) * float(number2)), 2)
                op_name = "multiplied by"
            case "4":
                if float(number2) == 0:
                    raise ZeroDivisionError

                answer = round((float(number1) / float(number2)), 2)
                op_name = "divided by"

    except ZeroDivisionError:
        return display_error_result(lang)

    return display_result(lang, op_name, number1, number2, answer)

def display_error_result(lang):
    # Displays any errors arising out of calculator operations
    message(data[lang]["zero_division_error"])

def display_result(lang, op_name, number1, number2, answer):
    output = data[lang]['output_ans']
    output = output.format(number1=number1, number2=number2, op_name=op_name, answer=answer)
    message(output)

def clear_screen():
    # Clearing the screen
    if os.name == 'nt':
        os.system('cls') # For windows
    else:
        os.system('clear') # For mac OS & Unix

def goodbye_message(lang):
    if RE_RUN in ['n', 'no', 'nah']:
        message(data[lang]["thank_you"])

message(data["en"]["welcome"]) # Prints welcome message

# Gets the language input only at the beginning
lang = display_language_choices(data["en"]["language_message"])

# Calculator begins
while RE_RUN not in ['n', 'no', 'nah'] or RE_RUN in ['yes', 'y', 'yeah']:
    number1 = get_number(lang, 'input_first_number') # Gets first number
    number2 = get_number(lang, 'input_second_number') # Gets second number
    operation = prompt_operator(lang, 'valid_operations')
    calculate(operation, number1, number2) # Performs calculator oeprations

# Asking if the user needs to use the calculator again
    message(data[lang]["calculate_again"])
    RE_RUN = input().lower()

    if RE_RUN not in ['yes', 'y', 'yeah']:
        if RE_RUN in ['n', 'no', 'nah']:
            goodbye_message(lang)
            break

        message(data[lang]["invalid_re_run_input"])
        continue

    clear_screen() # Clears the terminal screen for new calculation