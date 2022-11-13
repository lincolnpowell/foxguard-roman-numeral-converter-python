import scripts


# This function returns true when all characters within the string
# parameter are valid Roman numerals; else, return false.
def validate_input(string):
    roman_numerals = set(scripts.get_roman_numerals().keys())
    if all(numeral in roman_numerals for numeral in string):
        return True
    else:
        raise ValueError("Inputted string contains invalid characters")
