arr=[]
op=0
def opcion1():
        dato= input("Escribe el dato a agregar: ")
        if dato=="":
            print("No se agrego nada")
        else:
            arr.append(dato)
            print("Dato agregado")
def opcion2():
        if not arr:
            print("El arreglo esta vacio")
        else:
            print("El arreglo es: ")
            for i, v in enumerate (arr):
                print(f"Indice{i}:{v}")
def opcion3():
        if not arr:
            print("El arreglo esta vacio, no se puede eliminar")
        else:
            dato = input("Escribe el dato a eliminar: ")
            if dato in arr:
                arr.remove(dato)
                print("Dato eliminado")
            else:
                print("Dato no encontrado en el arreglo")
def opcion4():
        if not arr:
            print("El arreglo esta vacio, no se puede eliminar")
        else:
            i=int(input("Escribe el indice del dato a buscar: "))
            if 0 <=i < len(arr):
                nuevo_dato= input("Escribe el nuevo dato: ")
                arr[i] = nuevo_dato
                print("Dato modificado")
            else:
                print("Indice fuera de rango")
def opcion5():
        if not arr:
            print("El arreglo esta vacio")
        else:
            dato=input("Escribe el dato a buscar: ")
            indice =[i for i,v in enumerate(arr) if v ==dato]
            if indice:
                print(f"El dato entre {dato} se encuentra en la posicion {indice}")
            else:
                print("El dato no se encuentra en el arreglo")
def opcion6():
        print("Fin del programa")
opcion=0
while opcion!= 6:
    print("""
    --MENU ARREGLOS--
    1.- Agregar datos
    2.- Mostrar el arreglo
    3.- Eliminar dato
    4.- Modificar dato
    5.- Buscar dato
    6.- Salir
    """)
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        opcion1()
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        opcion3()
    elif opcion == 4:
        opcion4()
    elif opcion == 5:
        opcion5()
    elif opcion == 6:
        opcion6()
    else:
        print("Opción no válida, por favor elige una opción del 1 al 6.")


