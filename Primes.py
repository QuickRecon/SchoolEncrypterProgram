import math
import random


class Primes:

    @classmethod
    def compute_custom_prime(self, minimum, maximum):
        p = 100
        while not self.is_prime(int(p)):
            p = math.floor(random.random() * ((maximum - 1) - minimum + 1)) + minimum
            if self.is_prime(int(p)):
                print(p)
                return p

    @classmethod
    def is_prime(self, n):
        """isprime(n) - Test whether n is prime using a variety of pseudoprime tests."""
        if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            return True
        return self.is_prime_e(n, 2) and self.is_prime_e(n, 3) and self.is_prime_e(n, 5)

    @classmethod
    def is_prime_f(self, n, b):
        """isprimeF(n) - Test whether n is prime or a Fermat pseudoprime to base b."""
        return pow(b, n - 1, n) == 1

    @classmethod
    def is_prime_e(self, n, b):
        """isprimeE(n) - Test whether n is prime or an Euler pseudoprime to base b."""
        if not self.is_prime_f(n, b): return False
        r = n - 1
        while r % 2 == 0: r //= 2
        c = pow(b, r, n)
        if c == 1: return True
        while 1:
            if c == 1: return False
            if c == n - 1: return True
            c = pow(c, 2, n)
