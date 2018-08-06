class ListLogger(list):

    def __init__(self):
        super().__init__()
        print('Lista creada')

    def append(self, n):
        print('Agregando elemento a lista')
        super().append(n)


list_logger = ListLogger()
list_logger.append(10)
print(list_logger[0])
