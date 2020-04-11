# -*- coding: utf-8 -*-
"""
This package contains a variety of functions that often get reused when solving
Project Euler (projecteuler.net) problems.
"""
import math
from math import gcd as bltin_gcd


def divisors(n):
    """Returns a list of divisors of n
    
    Args:
        n (int): The number whose divisors will be returned
        
    Returns:
        divisors (list): List of divisors of n
    
    """
    divisors = [1]
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n/i:
                divisors += [int(i)]
            else:
                divisors += [int(i), int(n/i)]
    return divisors


def prime_factors(n):
    """Returns a list of prime factors of n
    
    Args:
        n (int): The number whose prime factors will be returned
        
    Returns:
        prime_factors (list): List of prime factors of n
    
    """
    i = 2
    prime_factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def is_prime(n):
    '''Returns True if n is prime, otherwise False'''
    # SPECIALCASE: These are special cases that are not primes
    if n % 2 == 0 and n != 2 or n <= 1:
        return False

    # Look for a factor
    for i in range(3, int(n ** (0.5)) + 1, 2):
        # If there is a factor
        if n % i == 0:
            # Its not a prime number
            return False


def sieve_of_eratosthenes(n):
    """sieve_of_eratosthenes(n): return the list of the primes < n."""
    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]


def is_palindrome(n):
    """Returns True if integer n is a palindrome, otherwise False"""
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def is_pandigital(n):
    """Returns True if n is a pandigital integer, otherwise False
    
    An m-digit number is pandigital if it makes use of all digits 1 to m
    exactly once. Example: 2143 is a 4-digit pandigital number.
    
    Args:
        n (int): The number to determine if it's pandigital
        
    Returns:
        True or False
    """
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(str(n)) > 9:
        return False
    for i in range(1, len(str(n)) + 1):
        if digits[i - 1] not in str(n):
            return False
    return True


def is_permutation(a, b):
    """Returns True is the digits of b are a permutation of the digits of a"""
    a, b = list(str(a)), list(str(b))
    if len(a) != len(b):
        return False
    else:
        for item in a:
            if item not in b:
                return False
            else:
                b.remove(item)
        return True


def coprime(a, b):
    """Returns True if a is coprime to b, otherwise False"""
    return bltin_gcd(a, b) == 1


def totient(n):
    """Takes integer n and returns Euler's Totient function (phi(n))"""
    phi = n
    factors = set(prime_factors(n))
    for _ in factors:
        phi *= (1 - 1/_)
    return int(phi)


def generalized_hamming(x, n):
    """An integer is an n-Hamming number if
    it has no prime factors larger than n
    
    Args:
        x (int): The number that is being checked if it is n-Hamming
        n (int): The largest possible prime factor of x
        
    Returns:
        True if x is n-Hamming, otherwise False
    """
    primes = sieve_of_eratosthenes(n + 1)
    for prime in primes:
        while x % prime == 0:
            x /= prime
    if x > 1:
        return False
    else:
        return True
