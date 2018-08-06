class StackBase:
    #Construye una pila vacía.
    def __init__(self):
        self.items = []
        pass

    #Devuelve un entero, el numero de elementos en la pila.
    def size(self):
        return len(self.items)

    #Agrega un elemento al final de la pila
    def push(self, element):
        self.items.append(element)
        pass

    #Elimina un elemento del final de la pila y lo devuelve
    def pop(self):
        return self.items.pop(-1)

    #Devuelve un elemento del final de la pila sin eliminarlo
    def top(self):
        if self.empty() == True:
            return None
        else :
            return self.items[len(self.items) - 1]

    #Devulve TRUE si la pila esta vacia, en caso contrario devulve FALSE
    def empty(self):
        return self.items == []

    #Elimina todos los elementos de la pila
    def clear(self):
        self.items = []
        pass

    def __str__(self):
        return "(" + ", ".join(self.items) + ")"

stack = StackBase()

stack.push('elemento 1')
stack.push('elemento 2')
stack.push('elemento 3')
stack.push('elemento 4')
print(stack.size())
print(stack.items)
print(stack.pop())
print(stack.top())

print(stack.__str__())

stack.clear()
print(stack.empty())
print(stack.__str__())