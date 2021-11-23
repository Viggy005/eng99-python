from fizzbuzz import *

#user input ---> max number to hit
#verify_digits


# produce output
def test_fizzbuzz_output_3_retuns_fizz():
    assert fizzbuzz_output(3) == "Fizz"

def test_fizzbuzz_output_5_retuns_buzz():
    assert fizzbuzz_output(5) == "Buzz"

def test_fizzbuzz_output_15_retuns_fizz():
    assert fizzbuzz_output(15) == "FizzBuzz"

def test_fizzbuzz_output_7_retuns_fizz():
    assert fizzbuzz_output(7) == 7
