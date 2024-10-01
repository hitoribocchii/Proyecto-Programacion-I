def inputNum(min, max):
    num = int(input())
    while (num < min) or (num > max):
        print("[ERROR] Numero ingresado fuera de rango, intentelo nuevamente: ")
        num = int(input())
    return num

# Variables necesarias para las funciones
locomotoras = ["CNR CKD8", "ALCo RSD-35", "Pacific 4-6-2"]
maxVagones = 10

def cargarFormacion():
    """
    Función para ingresar los datos necesarios de la locomotora.
    SALIDA:
        int: Numero de locomotora
        int: Cantidad de vagones pullman
        int: Cantidad de vagones primera clase
        int: Cantidad de vagones camarote
    """
    # Carga de locomotora
    print("[INPUT] Ingrese la locomotora a utilizar")
    for i in range(len(locomotoras)): #Imprime las locomotoras disponibles
        print(f"[{i}] {locomotoras[i]} ", end="", sep="")
    print()
    numLocomotora = inputNum(0, len(locomotoras)-1)

    print(f"[INFORMACIÓN] La cantidad maxima de vagones es de {maxVagones}")
    # Selección camarote
    print("[INPUT] Ingrese la cantidad de vagones camarote")
    cantCamarote = inputNum(0, maxVagones)
    # Selección primera clase
    if cantCamarote != maxVagones:
        print(f"[INPUT] Ingrese la cantidad de vagones de primera clase ({maxVagones-cantCamarote} restantes)")
        cantPrimera = inputNum(0, maxVagones-cantCamarote)
    # Selección pullman
    if cantCamarote + cantPrimera != maxVagones:
        print(f"[INPUT] Ingrese la cantidad de vagones de pullman ({maxVagones-cantCamarote-cantPrimera} restantes)")
        cantPullman = inputNum(0, maxVagones-cantCamarote-cantPrimera)
    

    print("Locomotora:", locomotoras[numLocomotora])
    print("Cantidad de vagones:", cantPullman + cantPrimera + cantCamarote)
    print("Vagones pullman:", cantPullman)
    print("Vagones primera clase:", cantPrimera)
    print("Vagones camarote:", cantCamarote)

    return numLocomotora, cantPullman, cantPrimera, cantCamarote

def main():
    cargarFormacion()

main()