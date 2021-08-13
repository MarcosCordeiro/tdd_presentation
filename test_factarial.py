import pytest
from factorial import factorial

#happy path
def test_factorial_type():
    assert type(factorial(0))==int

def test_factorial_with_3():
    assert factorial(3)==6

def test_factorial_with_4():
    assert factorial(4)==24

def test_factorial_with_negative():
    assert factorial(-1)==0

def test_factorial_with_negative_two():
    assert factorial(-2)==0

def test_factorial_with_negative_zero():
    assert factorial(0)==1

def test_factorial_with_non_number():
    with pytest.raises(ValueError) as ex:
        factorial('$')
    assert 'Invalid Input' in str(ex.value)

def test_factorial_with_non_number_raise():
    with pytest.raises(ValueError, match='Invalid Input'):
        factorial('a')

def test_factorial_with_math():
    assert factorial(3)==(3*2*1)

def test_factorial_with_math_2():
    assert factorial(5)==(factorial(4) * 5)
