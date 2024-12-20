import pytest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

@pytest.fixture()
def my_fixture():
    return Calculator()

# obj = Calculator()
#
# def test_add(obj):
#     assert obj.add(1,3) == 5

def test_multiply(my_fixture):
    assert my_fixture.multiply(1,3) == 65

def test_add(my_fixture):
    assert my_fixture.add(1, 3) == 5

# TODO TC01: Add the parametrization decorator and then, change the function below to use it
# def test_add():
#     pass


# # TODO TC02: Change the function below to assert about expected exceptions
# def test_divide():
#     pass