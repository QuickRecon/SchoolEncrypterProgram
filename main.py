from Encrypter import *

encrypted = []
decrypted = []

mode = input("\"Encrypt\", \"Decrypt\" or \"Encrypt and generate keypair\": ")

if mode == "Encrypt":
    encrypter = Encrypter()
    message = input("Enter Message: ")
    print("I will load the file \"PublicKey.txt\" to read the public key.")
    text_file = open("PublicKey.txt", "r")
    publickey = text_file.readline().split(',')
    blocks = encrypter.convert_text_to_block_array(message)
    for i in blocks:
        encrypted.append(encrypter.encrypt(i, publickey))
    print(message)
    print("This will overwrite \"Encrypted.txt\".")
    permission = input("Is this ok? (\"yes\", \"no\")")
    if permission == "yes":
        with open("Encrypted.txt", "w") as text_file:
            text_file.write(str(encrypted)[1:-1].replace(" ", ""))
        print("Your message has been written to Encrypted.txt.")
        print(encrypted)
    else:
        print("Exiting")

elif mode == "Decrypt":
    encrypter = Encrypter()
    print("I will load the file \"Encrypted.txt\" to read the message.")
    text_file = open("Encrypted.txt", "r")
    encrypted = text_file.readline().split(',')
    print("I will load the file \"PublicKey.txt\" to read the public key.")
    text_file = open("PublicKey.txt", "r")
    publickey = text_file.readline().split(',')
    print("I will load the file \"PrivateKey.txt\" to read the private key.")
    text_file = open("PrivateKey.txt", "r")
    privatekey = int(text_file.readline())
    for i in encrypted:
        decrypted.append(encrypter.decrypt(int(i), publickey, privatekey))
    print("Decrypted: " + encrypter.convert_block_array_to_text(decrypted))

elif mode == "Encrypt and generate keypair":
    encrypter = Encrypter()
    message = input("Enter your message:")
    print("Generating Keypair, this may take a while.")
    encrypter.generate_key_pair()
    blocks = encrypter.convert_text_to_block_array(message)
    for i in blocks:
        encrypted.append(encrypter.encrypt(i, encrypter.public_key))
    print(message)
    print("This will overwrite \"Encrypted.txt\", \"PublicKey.txt\" and \"PrivateKey.txt\".")
    permission = input("Is this ok? (\"yes\", \"no\")")
    if permission == "yes":
        with open("PrivateKey.txt", "w") as text_file:
            text_file.write(str(encrypter.private_key))
        with open("PublicKey.txt", "w") as text_file:
            text_file.write(str(encrypter.public_key)[1:-1].replace(" ", ""))
        with open("Encrypted.txt", "w") as text_file:
            text_file.write(str(encrypted)[1:-1].replace(" ", ""))
        print("Your message has been written to Encrypted.txt.")
        print(encrypted)
    else:
        print("Exiting")
