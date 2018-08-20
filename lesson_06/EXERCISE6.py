import re
class CipherBase:

    def __init__(self, encrypt_message, frecuency ):
        self.encrypt_message =  encrypt_message
        self.decrypt_message = ""
        self.frecuency= frecuency
        pass

    def __decrypt(self):
        count = {}
        for i in self.encrypt_message.lower():
            if re.match((r'[a-z]'),i)!= None: # Use re.math solo por jugar con .isalpha() salia igual
                if  i in count.keys():
                    count[i] = count[i] + 1
                else:
                    count[i] = 1
        l = list(count.items())
        l.sort(key=lambda x:x[1], reverse=True)

        frec = list(zip( self.frecuency.lower(), range(27)))

        comparacion = dict((l[i][0], frec[i][0]) for i in range(0, len(l)) )

        self.decrypt_message = ""
        for i in self.encrypt_message:
            if i.isalpha():
                if i.isupper() :
                    self.decrypt_message  += str(comparacion[i.lower()]).upper()
                elif i.islower():
                    self.decrypt_message  += str(comparacion[i])
            else:
                self.decrypt_message  += i 

        return self.decrypt_message 





    def print_decrypt_message(self):
        self.__decrypt()
        print(self.decrypt_message)
        

    def __str__(self):
        pass


mensaje_cifrado = '''
 Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe'l lgjb.
    Xof adpf vflqanfe logjbvn'x hf pdwqna d cgebv qn coqro xof tbdkfe ql mjlx d lpdbb tdex. Xof tbdkfe QL XOF HGLL; qx'l kgje vjxk xg fnxfexdqn oqp ge ofe.
    Zgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.
    Xof rglx gz dvvqna d zfdxjef qln'x mjlx xof xqpf qx xdwfl xg rgvf qx. Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn. Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgn'x zqaox fdro gxofe. - Mgon Rdepdrw.

    (ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)

    (ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)
    '''
frecuencia = "TEOAISRHNUCMDLGWFPYKJBVQX"
example_cipher = CipherBase(mensaje_cifrado, frecuencia)
example_cipher.print_decrypt_message()

