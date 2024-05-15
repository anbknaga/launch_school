import os
import math
import json
import sys

RE_RUN = ['y', 'yes', 'yeah']

try:
    with open('mortgage_messages.json', 'r') as file:
        data = json.load(file) # data has the contents of the json file
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

def messages(text):
    # Prints the text to be shown in the UI
    print("===> " + text)

def choose_language():
    # Displays available languages & get user input
    language = ['en', 'tm', 'hi']
    messages(data["en"]["lang_options"])
    langs = input().lower()
    while langs not in language:
        messages(data["en"]["lang_invalid"])
        langs = input().lower()
    return langs

def check_valid_numerical(number):
    # Check of invalid numerical inputs such as NaN or inf
    if math.isnan(float(number)) or math.isinf(float(number)):
        return False
    if float(number) <= 0:
        return False
    return True

def is_valid(number):
    # Logic for finding whether a number is valid
    try:
        float(number)
        return check_valid_numerical(number)
    except ValueError:
        return False

def get_inputs(langs, input_text):
    messages(data[langs][input_text])
    input_value = input()

    while not is_valid(input_value):
         # Checks if the input is valid otherwise prompts for a new input
        messages(data[langs]["invalid_number"])
        input_value = input()

    return float(input_value)

def check_valid_arr_input(number):
    if math.isnan(float(number)) or math.isinf(float(number)):
        return False
    if float(number) < 0:
        return False
    return True

def valid_annual_rate(arr_input):
    # Logic for finding whether a number is valid
    try:
        float(arr_input)
        return check_valid_arr_input(arr_input)
    except ValueError:
        return False

def get_annual_rate_input(langs, input_text):
    # This is a separate function to get 0% ARR input
    messages(data[langs][input_text])
    arr_input = input()

    while not valid_annual_rate(arr_input):
         # Checks if the input is valid otherwise prompts for a new input
        messages(data[langs]["invalid_number"])
        arr_input = input()

    return float(arr_input)

def mortgage_calculation(loan_dur_year, annual_rate, loan_amount):
    loan_dur_months = (loan_dur_year) * 12
    annual_rate = (annual_rate) / 100
    monthly_rate = (annual_rate) / 12
    try:
        monthly_payment = (loan_amount) * (
            monthly_rate / (1 - (1 + (monthly_rate)) ** ((-loan_dur_months)))
            )
        return monthly_payment
    except ZeroDivisionError:
        monthly_payment = loan_amount / loan_dur_months
        return monthly_payment

def display_results(langs, monthly_payment, loan_amount,
                    annual_rate, loan_dur_year):
    output = data[langs]['result']
    output = output.format(monthly_payment=monthly_payment,
                           loan_amount=loan_amount, annual_rate=annual_rate,
                           loan_dur_year=loan_dur_year)
    messages(output)

def calculate_again(langs):
    while True:
        messages(data[langs]['calculate_again'])
        re_run = input().lower()
        if re_run in ['y', 'yes', 'yeah']:
            clear_screen()
            return True
        if re_run in ['n', 'no', 'nah']:
            clear_screen()
            messages(data[langs]['goodbye'])
            return False
        messages(data[langs]["invalid_re_run_input"])

def clear_screen():
    if os.name == 'nt':
        os.system('cls') # For windows
    else:
        os.system('clear') # For mac OS & Unix

def main():
    while True:
        loan_amount = get_inputs(lang, 'ask_loan_amount')
        annual_rate = get_annual_rate_input(lang, 'ask_annual_rate')
        loan_dur_year = get_inputs(lang, 'get_loan_duration')
    # This is where the monthly payment calculation goes
        monthly_payment = mortgage_calculation(
            loan_dur_year, annual_rate, loan_amount)
        if monthly_payment is not None:
            monthly_payment = round(monthly_payment, 2)
            display_results(lang, monthly_payment, loan_amount,
                            annual_rate, loan_dur_year)

        if not calculate_again(lang):
            break

messages(data['en']['intro'])
lang = choose_language() # Assignment for the language

main() # Calling main function where calculator logic resides