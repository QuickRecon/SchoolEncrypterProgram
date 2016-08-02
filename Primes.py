import math
import random

class Primes:

    Primes = []

    def __init__(self):
        self.getPrimes()

    def getPrimes(self):
        primefile = open('primes.txt')
        for line in primefile.splitlines():
            self.Primes.append(tuple(line.split(",")))

    def isprime(self, n):
        """isprime(n) - Test whether n is prime using a variety of pseudoprime tests."""
        if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            return True
        return self.isprimeE(n, 2) and self.isprimeE(n, 3) and self.isprimeE(n, 5)

    def isprimeF(self, n, b):
        """isprimeF(n) - Test whether n is prime or a Fermat pseudoprime to base b."""
        return pow(b, n - 1, n) == 1

    def isprimeE(self, n, b):
        """isprimeE(n) - Test whether n is prime or an Euler pseudoprime to base b."""
        if not self.isprimeF(n, b): return False
        r = n - 1
        while r % 2 == 0: r //= 2
        c = pow(b, r, n)
        if c == 1: return True
        while 1:
            if c == 1: return False
            if c == n - 1: return True
            c = pow(c, 2, n)
