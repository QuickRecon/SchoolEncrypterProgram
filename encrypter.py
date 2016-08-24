from Primes import *
import math


class Encrypter:
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    large_primes = []

    exponent = 3

    private_key = 0

    public_key = []

    totient = 0

    product = 0

    blocks = []

    def generate_key_pair(self):
        self.large_primes.append(int(Primes.compute_custom_prime(pow(2, 1011), pow(2, 1013))))
        self.large_primes.append(int(Primes.compute_custom_prime(pow(2, 1011), pow(2, 1013))))
        self.product = self.large_primes[0] * self.large_primes[1]
        self.totient = (self.large_primes[0] - 1) * (self.large_primes[1] - 1)
        self.generate_exponent()
        self.private_key = self.extended_euclidean(self.totient)
        self.public_key = [self.exponent, self.product]
        return [self.exponent, self.product]

    def extended_euclidean(self, totient):
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

    def generate_exponent(self):
        for i in self.small_primes:
            if math.gcd(i, self.totient) == 1:
                self.exponent = int(i)
                return i

    def convert_text_to_block_array(self, message):
        char_list = []
        blocks = []
        index = 0
        message = list(message)
        for i in message:
            char_list.append('%0*d' % (6, ord(i)))
        while index <= len(char_list):
            stage = "1"
            for i in range((len(str(self.product)) - 1) // 6):
                if index + i < len(char_list):
                    stage += char_list[index + i]
            blocks.append(int(stage))
            index += (len(str(self.product)) - 1) // 6
        return blocks

    def convert_block_array_to_text(self, block):
        text = []
        for w in block:
            item = str(w)[1:]
            item = self.split(item, 6)
            for i in item:
                text.append(chr(int(i)))
        return ''.join(text)

    def split(self, s, chunk_size):
        a = zip(*[s[i::chunk_size] for i in range(chunk_size)])
        return [''.join(t) for t in a]

    def encrypt(self, message, public_key):
        return pow(message, public_key[0], public_key[1])

    def decrypt(self, message, public_key, private_key):
        return pow(message, int(private_key), int(public_key[1]))


