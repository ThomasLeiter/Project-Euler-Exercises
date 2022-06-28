"""
If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

if __name__ == '__main__':
    # Brute-Force addition of suitable numbers
    sum_of_multiples = sum(
        n for n in range(1000) 
        if n % 3 == 0 or n % 5 == 0)
    print(f'The brute-force result is {sum_of_multiples}.')

    # Direct Calculation via 'Little Gauss Method' 
    # and Principle of Inclusion-Exclusion
    a,b,c = 999//3, 999//5, 999//15
    sum_of_multiples = 3*a*(a+1)//2 + 5*b*(b+1)//2 - 15*c*(c+1)//2
    print(f'The calculated sum is {sum_of_multiples}.')
