# Importar la clase Pila
import estructuras

def main():
    # Usar la clase Pila para crear objetos y añadir números a la pila
    
    # Usa la clase Pila. Crea una pila y añade los elementos 3, 6, 8, 9. 
    p = estructuras.Pila()
    p.push(3)
    p.push(6)
    p.push(8)
    p.push(9)
    print(p)

    # Crea otra segunda pila y añade 3 y 6. Muestralas por pantalla. Compara ambas pilas.
    p2 = estructuras.Pila()
    p2.push(3)
    p2.push(6)
    print(p2)
    print(p == p2)

    # Haz dos pops de la primera pila y muestra la pila por pantalla. Vuelve a compararlas. 
    p.pop()
    p.pop()
    print(p)
    print(p2)
    print(p == p2)


main()

