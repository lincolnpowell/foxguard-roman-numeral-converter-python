from scripts import convert_roman_numeral_to_integer, validate_input


def main():
    string = input('Enter Roman numeral string: ')
    try:
        validate_input(string)
    except ValueError as exception:
        print(exception)
    else:
        value = convert_roman_numeral_to_integer(string)
        print("The integer representation of", string, "is", value)


# Call the main function to run the program.
main()
