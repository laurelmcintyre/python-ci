import math

def factorial(x):
    if x > 0:
        y = math.factorial(x)
        return(y)

def test_myfactorial():
    assert(factorial(4))==24
    assert(factorial(7))==5040
    assert(factorial(1))==1