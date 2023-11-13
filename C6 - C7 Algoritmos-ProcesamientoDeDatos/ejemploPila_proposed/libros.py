# Define la clase Libro
class Libro:
    IVA = 10

    def __init__(self, autor, titulo, precio):
        self.__autor = autor
        self.__titulo = titulo
        self.__precio_base = precio

    @property   
    def autor(self):
        return self.__autor

    @property   
    def titulo(self):
        return self.__titulo

    @property   
    def precio_base(self):
        return self.__precio_base

    def precio_final(self):
        return self.__precio_base + self.__precio_base * Libro.IVA / 100

    def __str__(self):
        return f"({self.__autor}; {self.__titulo}; {self.__precio_base:.2f}; {Libro.IVA:.1f}%; {self.precio_final():.2f})"

    def __eq__(self, other):
        salida = False
        if isinstance(other, Libro):
            salida = self.__autor.lower() == other.autor.lower() and self.__titulo.lower() == other.titulo.lower()

        return salida