"""
Each new term in the Fibonacci sequence is 
generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

def fibonacci_generator(max):
    """
    Generate and yield fibonacci numbers
    up to a given maximum. \n
    The sequence starts with 1,2,3,5,8,...

    Parameter:
    -----------
    max : int
        The maximum number to yield
    
    Result:
    -----------
    int 
        The fibonacci sequence
    """
    a = 1
    yield a
    b = 2
    while b <= max:
        yield b
        a,b = b,a+b

if __name__ == '__main__':
    sum_of_even_fibonacci_numbers = sum(
        f for f in fibonacci_generator(4e6)
        if f % 2 == 0)
    print(f'The sum of even fibonacci numbers is {sum_of_even_fibonacci_numbers}.')