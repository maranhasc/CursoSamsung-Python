# Copiar la clase Pila del ejercicio anterior

class Pila:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        else:
            raise IndexError("La pila está vacía")
            
    def size(self):
        return len(self.__items)
    
    def __str__(self):
        cad = "["
        for l in self.__items:
            cad += str(l) + ",\n"
        cad = cad[:-2] + "]"
        return cad
    
    def __eq__(self, other):
        salida = False
        if isinstance(other, Pila):
            if (self.size() == other.size() and self.__items == other.__items):
                salida = True
        return salida
    