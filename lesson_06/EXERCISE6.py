class CipherBase:

    def __init__(self, encrypt_message):
        self.encrypt_message =  encrypt_message
        self.decrypt_message = ""


        pass

    def __decrypt(self):
        L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
        I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        key = 3
        for c in self.encrypt_message.upper():
            if c.isalpha():
                self.decrypt_message += I2L[(L2I[c] - key) % 26]
            else:
                self.decrypt_message += c
        pass

    def print_decrypt_message(self):
        print(self.decrypt_message)

    def __str__(self):
        pass


    cifrado = "TEOAISRHNUCMDLGWFPYKJBVQX"
    descifrado = "De mas frecuente a menos frecuente"



    print( len(cifrado))
    print( len(descifrado))

    #for i in list(cifrado):
    #    if i in descifrado.upper():
    #        print(descifrado.upper().index(i))

    #print(list(cifrado))