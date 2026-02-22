personas = []
id = 0
op = 0
def opcion1():
        global id,personas
        id = id + 1
        nombre = input("Nombre:")
        edad = input("Edad:")
        email = input("Email:")
        telefono = input("Telefono:")
        persona = {"id": id, "nombre": nombre, "edad": edad, "email": email, "telefono": telefono}
        personas.append(persona)
        print("Persona agregada")
def opcion2():
        global id,personas
        if not personas:
            print("no hay pesonas registradas")
        else:
            for p in personas:
                print(f"ID: {p['id']} Nombre: {p['nombre']} Edad: {p['edad']} Email: {p['email']} Telefono: {p['telefono']}")
                
def opcion3():
        global id,personas
        nom = input("Escribe e nombre a buscar: ")
        encontrados = [p for p in personas if nom in p['nombre']]
        if not encontrados:
            print("No existe el nombre en la lista")
        else:
            for p in encontrados:
                print(f"ID: {p['id']} Nombre: {p['nombre']} Edad: {p['edad']} Email: {p['email']} Telefono: {p['telefono']}")
def opcion4():
        global id,personas
        id_buscar = int(input("Escribe el ID a modificar: "))
        for p in personas:
            if p['id'] == id_buscar:
                print("Dar enter si se quiere dejar el valor actual")
                nNombre = input(f"Nombre:{p['nombre']}->")
                nEdad = input(f"Edad:{p['edad']}->")
                nEmail = input(f"Email:{p['email']}->")
                nTelefono = input(f"Telefono:{p['telefono']}->")
                if nNombre:
                    p['nombre'] = nNombre
                if nEdad:
                    p['edad'] = nEdad
                if nEmail:
                    p['email'] = nEmail
                if nTelefono:
                    p['telefono'] = nTelefono
                print("Persona modificada")
                break
        else:
            print("No existe el ID")
def opcion5():
        global id,personas
        id_buscar = int(input("Escribe el ID a borrar:"))
        for p in personas:
            if p['id'] == id_buscar:
                print("Persona borrada")
                personas.remove(p)
                break
        else:
            print("No existe el ID")
def opcion6():
        print("Fin del programa")
opcion=0
while opcion!= 6:
    print("""
    Menu personas****
    1. Agregar persona
    2. Listar personas
    4. Editar persona
    3. Buscar por nombre
    5. Eliminar persona
    6. Salir
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

