class CipherBase:

    def __init__(self, encrypt_message):
        self.encrypt_message =  encrypt_message
        self.decrypt_message = ""
        pass

    def __decrypt(self):
        L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
        I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

        print(L2I)
        print(I2L)
        key = 3
        for c in self.encrypt_message.upper():
            if c.isalpha():
                self.decrypt_message += I2L[(L2I[c] - key) % 26]
            else:
                self.decrypt_message += c
        pass

    def print_decrypt_message(self):
        self.__decrypt()
        return  (str(self.decrypt_message))

    def __str__(self):
        pass

cifrado = "TEOAISRHNUCMDLGWFPYKJBVQX"
descifrado = "De mas frecuente a menos frecuente"



example_cipher = CipherBase(cifrado)

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

print(cifrado)
print(example_cipher.print_decrypt_message())


print( len(cifrado))
print( len(descifrado))

cadena = []
for i in cifrado:
    for k, value in L2I.items():
           if i == k:
               cadena.append('{}: {}'.format(k, value))

print(cadena)
print(L2I.items())