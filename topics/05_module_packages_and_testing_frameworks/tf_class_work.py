import pytest
from pyexpat.errors import messages


def my_func(param: int) -> int:
    return param + 1

# for i in range(10):
#     # print(my_func(i)) = i + 1
#     assert

def divide (a: int, b: int) -> int | float:
    return a/b

@pytest.mark.parametrize(
    "dividend, divisor, expected",
    [
        (4,2,2),
        (6,6,1),
        (3,0,(ZeroDivisionError, "division by zero")),
        (-7,3,-2.3333333333333335),
        (-11.5,2,-5.75)
    ]
)
def test_divide(dividend, divisor, expected):
    # if divisor == 0:
    #     with pytest.raises(expected[0]):
    #         divide(dividend,divisor)
    # else:
    assert divide(dividend, divisor) == expected

def test_divide_negative():
    with pytest.raises(ZeroDivisionError, match = 'divission by zero'):
        divide(5,0)


@pytest.mark.parametrize(
    "my_input, expected",
    [
        (1,2),
        (2,3),
        (3,4),
        (4,5)
    ]
)
# first parameter - name of parameters;
# second - tuple of values

def test_my_func(my_input, expected):
    assert my_func(my_input) == expected
