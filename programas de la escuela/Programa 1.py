v= [0 for x in range(11)] #segenera un arreglo de 11 posiciones
n=0 #indica cuantos elementos tiene el arreglo
y=0 #agregar un dato a modificar
x=0 #agregar un nuevo dato o un dato a buscar
i=0 #es el indice dentro del arreglo
op=0

while op !=6:
    print("MENU DE ARREGLOS")
    print("1.- Agregar datos al arreglo")
    print("2.- Buscar datos en el arreglo")
    print("3.- Eliminar datos del arreglo")
    print("4.- Modificar datos del arreglo")
    print("5.- Mostrar el arreglo")
    print("6.- Salir")
    op = int(input("Seleccione una opcion: "))
    if op==1:
        if n <10:
            y=int(input("Escribe el valor a agregar: "))
            n=n+1
            v[n]=y
            print("Se agrego el valor " + str(y))
        else:
            input("El arreglo ya esta lleno")
    elif op==2:
        x= int(input("Escribe el valor a buscar: "))
        i=1
        while i<=n and x != v[i]:
            i=i+1
        if i>n:
            print("El dato "+str(x)+" no esta en el arreglo")
        else:
            print("El dato "+ str(x)+" esta en la posicion "+str(i))
    elif op==3:
        x= int(input("Escribe el valor a borrar: "))
        i=1
        while i<=n and x != v[i]:
            i=i+1
        if i>n:
            print("El dato "+str(x)+" no esta en el arreglo")
        else:
            for k in range(1,n):
                v[k]=v[k+1]
            n=n-1
            print("Se elimino el valor " +str(x))
    elif op==4:
        x= int(input("Escribe el valor a modificar: "))
        y= int(input("Escribe el nuevo valor: "))
        i=1
        while i<=n and x != v[i]:
            i=i+1
        if i>n:
            print("El dato "+str(x)+" no esta en el arreglo")
        else:
            v[i]=y
            print("Se modifico el arreglo")
    elif op==5:
        for i in range(1,n+1):
            print("[" +str(i)+ "]: " + str(v[i]))
    elif op==6:
        print("Fin del programa")
    else:
        print("Opcion no valida")