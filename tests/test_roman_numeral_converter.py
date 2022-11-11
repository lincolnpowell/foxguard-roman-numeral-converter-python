from scripts import convert_roman_numeral_to_integer


class TestRomanNumeralConverter:
    def test_conversions(self):
        assert convert_roman_numeral_to_integer("XIII") == 13
        assert convert_roman_numeral_to_integer("LV") == 55
        assert convert_roman_numeral_to_integer("XLIX") == 49
        assert convert_roman_numeral_to_integer("DCCLXXXIX") == 789
