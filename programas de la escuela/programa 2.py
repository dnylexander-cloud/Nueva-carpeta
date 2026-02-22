arr=[]
op=0

while op !=6:
    print("""
          --MENU ARREGLOS--
          1.- Agregar datos
          2.- Mostrar el arreglo
          3.- Eliminar dato
          4.- Modificar dato
          5.- Buscar dato
          6.- Salir
          """)
    op = int(input("Seleccione una opcion: "))
    if op==1:
        dato= input("Escribe el dato a agregar: ")
        if dato=="":
            print("No se agrego nada")
        else:
            arr.append(dato)
            print("Dato agregado")

    if op==2:
        if not arr:
            print("El arreglo esta vacio")
        else:
            print("El arreglo es: ")
            for i, v in enumerate (arr):
                print(f"Indice{i}:{v}")
    
    if op==3:
        if not arr:
            print("El arreglo esta vacio, no se puede eliminar")
        else:
            dato = input("Escribe el dato a eliminar: ")
            if dato in arr:
                arr.remove(dato)
                print("Dato eliminado")
            else:
                print("Dato no encontrado en el arreglo")
        
    if op==4:
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
    if op==5:
        if not arr:
            print("El arreglo esta vacio")
        else:
            dato=input("Escribe el dato a buscar: ")
            indice =[i for i,v in enumerate(arr) if v ==dato]
            if indice:
                print(f"El dato entre {dato} se encuentra en la posicion {indice}")
            else:
                print("El dato no se encuentra en el arreglo")
    if op==6:
        print("Fin del programa")