"""
Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions 
for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 
1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 
in ascending order of size, find the numerator of the fraction 
immediately to the left of 3/7.
"""

def gcd(a,b):
    """
    Calculate the greatest common divisior \n
    using Euklid's algorithm.

    Parameters:
    ------------
    a,b : int
        The two integers to find the gcd of
    
    Returns:
    ---------
    int
        The gcd of a and b
    """
    if b == 0:
        return a
    return gcd(b,a%b)

def less_than(lhs_num,lhs_den,rhs_num,rhs_den):
    return lhs_num * rhs_den < lhs_den * rhs_num

def binary_numerator_search(denominator,n,d):
    lo,hi = 0,denominator
    while hi-lo>1:
        mi = (hi+lo)//2
        if less_than(mi,denominator,n,d):
            lo = mi
        else:
            hi = mi
    return lo

def farey_sequence(max_denominator,n,d):
    """
    Calculates the best left approximation of \n
    n/d with a denominator <= max_denominator using \n
    the farey sequence, which calculates intermediate \n
    values of fractions a/b and c/d as (a+c)/(b+d) and \n
    can be proved to yield the best approximation \n
    up to any limit.

    Parameters:
    ------------
    max_denominator : int
        The maximum denominator allowed
    n,d : int
        Numerator and denominator of the 
        positive fraction to approximate

    Returns:
    ---------
    (int,int)
        The best left approximation as 
        a numerator,denominator pair
    """
    lo_num,lo_den = 0,1
    hi_num,hi_den = 1,0
    while True:
        mi_num = lo_num + hi_num
        mi_den = lo_den + hi_den
        if mi_den > max_denominator:
            return lo_num,lo_den
        if less_than(mi_num,mi_den,n,d):
            lo_num,lo_den = mi_num,mi_den
        else:
            hi_num,hi_den = mi_num,mi_den
        

if __name__ == '__main__':
    n,d = 3,7
    max_denominator = 10**6
    """
    # Naive search over all denominators

    best_num,best_den = 0,1
    for den in range(2,max_denominator+1):
        num = binary_numerator_search(den,n,d)
        if less_than(best_num,best_den,num,den) and gcd(num,den)==1:
            best_num,best_den = num,den
            print(f'New best left approximation of {n}/{d}: {num}/{den}.')
    print(f'Best left approximation of {n}/{d}: {best_num}/{best_den}.')
    """
    best_num,best_den = farey_sequence(max_denominator,n,d)
    print(f'Best left approximation of {n}/{d}: {best_num}/{best_den}.')
