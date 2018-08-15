# Ejercicio #

## Cipher ##

Debes construir una clase llamada Cipher con la finalidad de desencriptar mensajes nazis ocultos, por ejemplo:

    Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe'l lgjb.
    Xof adpf vflqanfe logjbvn'x hf pdwqna d cgebv qn coqro xof tbdkfe ql mjlx d lpdbb tdex. Xof tbdkfe QL XOF HGLL; qx'l kgje vjxk xg fnxfexdqn oqp ge ofe.
    Zgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.
    Xof rglx gz dvvqna d zfdxjef qln'x mjlx xof xqpf qx xdwfl xg rgvf qx. Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn. Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgn'x zqaox fdro gxofe. - Mgon Rdepdrw.

    (ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)

    (ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)

Se sabe que sólo se han encriptado las letras del alfabeto (a - z). Te ayudaremos con la frecuencia de apariciones de las letras
en el mensaje desencriptado.

    freq = "TEOAISRHNUCMDLGWFPYKJBVQX" # De mas frecuente a menos frecuente

La clase que crees debe heredar de la siguiente interfaz:

encrypt_message = '''
    Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe'l lgjb.
    Xof adpf vflqanfe logjbvn'x hf pdwqna d cgebv qn coqro xof tbdkfe ql
    mjlx d lpdbb tdex.
    Xof tbdkfe QL XOF HGLL; qx'l kgje vjxk xg fnxfexdqn oqp ge ofe.
    Zgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.
    Xof rglx gz dvvqna d zfdxjef qln'x mjlx xof xqpf qx xdwfl xg rgvf qx.
    Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn.
    Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgn'x zqaox fdro gxofe.
    - Mgon Rdepdrw.
    (ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)
    (ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)
    '''

freq = 'TEOAISRHNUCMDLGWFPYKJBVQX'

letras_encriptadas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'

dic = {}
l = []
for letra in encrypt_message :
    if letra in letras_encriptadas :
        if letra.upper() in dic:
            dic[letra.upper()] += 1
        else :
            dic[letra.upper()] = 1

dic = dict(sorted(dic.items() , key=lambda x : x[1] , reverse=True))
print(dic)
freq_encriptada = ''.join(k for k in dic.keys())

mensaje_desincretado = ''

for letra in encrypt_message :
    almacenar = freq_encriptada.find(letra.upper())
    letra_desincreptadas = freq[almacenar]

    if almacenar > -1 :
        if letra.isupper():
            mensaje_desincretado += letra_desincreptadas.upper()
        else :
            mensaje_desincretado += letra_desincreptadas.lower()
    else:
            mensaje_desincretado += letra
print(mensaje_desincretado)
