# X Ask the user for the first number
# X Ask the user for the second number
# X Ask the user for the operation they would like to perform
# X Perform the operation
# X Print the result

def message(prompt):
    print("==> " + prompt)

# Logic for finding if a number is valid or not
def invalid_number(number):
    try:
        float(number)
    except ValueError:
        return True

    return False

RE_RUN = 'y'

while RE_RUN not in ['n', 'no', 'nah'] or RE_RUN in ['yes', 'y', 'yeah']:

    message("THE CALCULATOR <==\n")

    message("Enter the value for the first number: ")
    number1 = input()

    # Checks if the input is valid otherwise prompts for a new input
    while invalid_number(number1):
        message("Please enter a valid number for the first number")
        number1 = input()

    message("Enter the value for the second number: ")
    number2 = input()

    # Checks if the input is valid otherwise prompts for a new input
    while invalid_number(number2):
        message("Please enter a valid number for the second number")
        number2 = input()

    # Asking the user for what operation they would like to perform

    message("Menu:\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "Select a number from the menu: ")

    operation = input()

    while operation not in ['1', '2', '3', '4']:
        message("Invalid input.\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "Select a number from the menu: ")
        operation = input()

    #Performing the operation

    match operation:
        case "1":
            answer = float(number1) + float(number2)
            answer = round(answer, 2)
            OP_NAME = "addition"
            message(f"\nThe result of the {OP_NAME} operation is {answer}\n")
        case "2":
            answer = float(number1) - float(number2)
            OP_NAME = "subtraction"
            message(f"\nThe result of the {OP_NAME} operation is {answer}\n")
        case "3":
            answer = float(number1) * float(number2)
            OP_NAME = "multiplication"
            message(f"\nThe result of the {OP_NAME} operation is {answer}\n")
        case "4":
            try:
                answer = float(number1) / float(number2)
                answer = round(answer, 2)
                OP_NAME = "division"
                message(f"\nThe result of the {OP_NAME} is {answer}\n")
            except ZeroDivisionError:
                print("Cannot divide by zero")

    RE_RUN = input("Do you want to calculate again? (y/n): ").lower()
    while RE_RUN not in ['n', 'no', 'nah', 'yes', 'y', 'yeah']:
        message("Invalid input. Enter 'y' or 'n': ")
        RE_RUN = input()
    if RE_RUN in ['n', 'no', 'nah']:
            message("Thank you for using the calculator :) See you again soon")