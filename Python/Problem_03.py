"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def prime_sievle(N):
    """
    Implementation of the sievle of Erastothenes. \n
    Calculate the list of all prime numbers not \n
    exceeding N.

    Parameters:
    ------------
    N : int
        The upper limit of the sievle range
    
    Result:
    --------
    list[int]
        The list of all primes up to N
    """
    lst = [n for n in range(N+1)]
    p = 2
    while p*p <= N:
        for t in range(p*p,N+1,p):
            lst[t] = 0
        p += 1
        while p*p <= N and lst[p] == 0:
            p += 1
    return [n for n in range(2,N+1) if lst[n]]

def factorize(N,prime_list):
    """
    Factorize N using a list of primes. \n
    For exact results, ensure  \n
    max(prime_list) >= sqrt(N).

    Parameters:
    ------------
    N : int
        The number to factorize
    prime_list : list[int]
        A list of primes [2,3,5,...]
    
    Result:
    --------
    list[int]
        The factorization of N
    """
    prime_factors = []
    for p in prime_list:
        while N % p == 0:
            prime_factors.append(p)
            N //= p
        if N == 1:
            return prime_factors
    prime_factors.append(N)
    return prime_factors


if __name__ == '__main__':
    N = 600851475143
    primes = prime_sievle(int(N**.5))
    factorization = factorize(N,primes)
    print(f'{N} can be factorized into {factorization}.')
    print(f'The largest prime factor is therefore {factorization[-1]}.')