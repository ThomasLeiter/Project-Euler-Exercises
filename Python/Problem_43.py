"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def generate_pandigital_numbers(
    digits={0,1,2,3,4,5,6,7,8,9},
    prefix=0,
    suffix=0,
    divisors=[1,1,1,2,3,5,7,11,13,17]):
    """
    Generate the pandigital numbers, that 
    have successive digit triplets divisible
    by the given list of prime divisors.

    Parameters:
    ------------
    digits : set[int]
        The set of decimal digits
    prefix : int
        The number formed by the leading digits
    suffix : int
        The number formed by the three trailing digits
    divisors : list[int]
        The list of prime divisors lead by three dummy 1s

    Returns:
    ---------
    Iterator[int]
        A generator of all pandigital numbers
        meeting the divisibility criterion
    """
    if not divisors:
        yield prefix
    suffix = (suffix % 100) * 10
    prefix *= 10
    for d in digits:
        if (suffix + d) % divisors[0] == 0:
            yield from generate_pandigital_numbers(
                digits - {d},
                prefix + d,
                suffix + d,
                divisors[1:])

if __name__ == "__main__":
    sum_of_pandigitals = sum(generate_pandigital_numbers())
    print(f"The sum of suitable pandigitals is {sum_of_pandigitals}.")