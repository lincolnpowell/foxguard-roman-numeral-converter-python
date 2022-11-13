import scripts


# This function iterates through a Roman numeral string, converts
# each character to its integer representation and calculates the full
# representation of the string to the overall integer value.
def convert_roman_numeral_to_integer(string):
    result = 0

    index = 0
    for char in string:
        current_value = scripts.get_roman_numeral_value(char)
        next_value = 0
        if index + 1 != len(string):
            next_value = scripts.get_roman_numeral_value(string[index + 1])

        if current_value >= next_value:
            result += current_value
        else:
            result -= current_value

        index += 1

    return result
