# X Ask the user for the first number
# X Ask the user for the second number
# X Ask the user for the operation they would like to perform
# Perform the operation
# Print the operation

def prompt(message):
    print(f"===> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt("THE CALCULATOR\n")

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmmm... this is not a valid number")
    number1 = input()

prompt("Enter the second number: ")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

operation = input("\nFollowing operations are supported in this calculator: "
                  "       \n'A' - Addition"
                  "       \n'S' - Subtraction"
                  "       \n'M' - Multiplication"
                  "       \n'D' - Division\n"
                  "Enter here: ").lower() # case insensitivity is handled here

while operation not in ["a", "s", "m", "d"]:
    prompt("select only from the given options: a, s, m, d: ")
    operation = input()

# Performing calculations

match operation:
    case 'a':
        output = int(number1) + int(number2)

    case 's':
        output = int(number1) - int(number2)

    case 'm':
        output = int(number1) * int(number2)

    case 'd':
        output = int(number1) / int(number2)

print(f"\nThe output of the operation is {output}\n")
