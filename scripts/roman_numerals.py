roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def get_roman_numerals():
    return roman_numerals


def get_roman_numeral_value(key):
    return roman_numerals.get(key)
