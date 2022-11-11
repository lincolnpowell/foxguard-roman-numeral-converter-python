import pytest

from scripts import validate_input


class TestInputValidator:
    def test_successful_user_input(self):
        if validate_input("IV"):
            pass
        else:
            pytest.fail()

    def test_invalid_user_input(self):
        with pytest.raises(ValueError) as exception:
            validate_input("AX")
        assert str(exception.value) ==\
               "Inputted string contains invalid characters"
