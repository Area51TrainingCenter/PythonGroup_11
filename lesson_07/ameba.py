class Ameba:

    def __init__(self, name):
        self.name = name
        print('Creando Ameba')

# Se está harcodeando el nombre de clase, lleva a problemas cuando se usa herencia
#   def mitosis(self, name):
#       ameba = Ameba(name)
#       return ameba

    @classmethod
    def mitosis(cls, name):
        ameba = cls(name)
        return ameba


class AmebaImproved(Ameba):
    def __init__(self, name):
        self.name = name
        print('Creando Ameba Mejorada')


ameba1 = Ameba('ameba1')
ameba2 = ameba1.mitosis('ameba2')
print(ameba1.name)
print(ameba2.name)

ameba_improved1 = AmebaImproved('ameba1')
ameba_improved2 = ameba_improved1.mitosis('ameba2')
print(ameba_improved1.name)
print(ameba_improved2.name)

