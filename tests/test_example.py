import pytest

from scripts import Example


class TestExample:
    def test_make_one_example(self):
        example = Example("hello world")
        assert example.get_message() == "hello world"

    def test_invalid_example_initialization(self):
        with pytest.raises(ValueError) as exception:
            Example("")
        assert str(exception.value) == "Invalid message"
