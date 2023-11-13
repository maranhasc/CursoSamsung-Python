import estructuras as e
from libros import Libro
import numpy as np

def main():
     p = e.Pila()
     l1 = Libro("george orwell", "1984", 8.20)
     l2 = Libro("Philip K. Dick", "¿Sueñan los androides con ovejas eléctricas?", 3.50)
     l3 = Libro("Isaac Asimov", "Fundación e Imperio", 9.40)

     
     p.push(l1)
     p.push(l2)
     p.push(l3)

     print("Mostramos la pila")   
     print(p)

     l = p.pop()
     print("Mostramos el libro")   
     print(l)

     print("Mostramos la pila")   
     print(p)

     z = np.zeros(3,3)

main()
