from Primes import *
from fractions import gcd



class Encrypter:
    smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    largeprimes = []

    exponent = 3

    privatekey = 0

    publickey = []

    totient = 0

    product = 0

    blocks = []

    def genkeypair(self):
        self.largeprimes.append(int(Primes.computeCustomPrime(10 ** 10, 10 ** 15)))
        self.largeprimes.append(int(Primes.computeCustomPrime(10 ** 10, 10 ** 15)))
        self.product = self.largeprimes[0] * self.largeprimes[1]
        print("n = " + str(self.product))
        self.totient = (self.largeprimes[0] - 1) * (self.largeprimes[1] - 1)
        print("toitent = " + str(self.totient))
        self.generateexponent()
        print("Exponenet = " + str(self.exponent))
        print("Generating keys")
        self.privatekey = self.extendedeuclidean(self.totient)
        print("private = " + str(self.privatekey))
        self.publickey = [self.exponent, self.product]
        print("public = " + str(self.publickey))
        return [self.exponent, self.product]

    def extendedeuclidean(self, totient):
        column1_old = totient
        column2_old = totient
        column1 = self.exponent
        column2 = 1
        while True:
            # print("iterating")
            column1_new = column1_old // column1
            column2_new = column1_new * column2
            column1_new *= column1
            column1_stage = column1_old - column1_new
            column2_stage = column2_old - column2_new
            column1_old = column1
            column2_old = column2
            column1 = column1_stage
            column2 = column2_stage
            if column2 <= 0:
                column2 = column2 % totient
            if column1 <= 1:
                return column2

    def generateexponent(self):
        for i in self.smallprimes:
            if gcd(i, self.totient) == 1:
                self.exponent = int(i)
                return i

    def converttexttoblockarray(self, message):
        if len(str(message)) > len(str(self.product)):
            self.blocks = map(''.join, zip(*[iter(str(message))]*len(str(self.product))))


    def encrypt(self, message, publickey):
        return pow(message, publickey[0], publickey[1])

    def decrypt(self, message, publickey):
        return pow(message, self.privatekey, publickey[1])
