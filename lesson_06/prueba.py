import operator

frase = str(
    'Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe l lgjb.Xof adpf vflqanfe logjbvnx hf pdwqna d cgebv qn coqro xof tbdkfe ql mjlx d lpdbb tdex. Xof tbdkfe QL XOF HGLL; qxl kgje vjxk xg fnxfexdqn oqp ge ofe.Zgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.    Xof rglx gz dvvqna d zfdxjef qlnx mjlx xof xqpf qx xdwfl xg rgvf qx. Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn. Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgnx zqaox fdro gxofe. - Mgon Rdepdrw.(ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)    (ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)))')
frec = {}
for i in frase:
    if i.isalpha():
        if i.lower() not in frec.keys():
            frec[i.lower()] = 1
        else:
            frec[i.lower()] += 1

#print(sorted(frec))

orden = []
print(list(frec.items()))
l = list(frec.items())
l.sort(key=lambda x: x[1])
print(l)

    #    if orden[k]


print(orden)