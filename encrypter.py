from Primes import *


class Encrypter:

    primes = Primes

    def __init__(self):
        self.primes = Primes()

    def genkeypair(self):
        self.primes.computePrimes(pow(10,100), pow(10,101))



