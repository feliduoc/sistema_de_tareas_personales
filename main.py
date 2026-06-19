print("--- Bienvenido al Sistema de Tareas Personales :D ---")
#lunes 15, cree el archivo ,py y puse el mensaje de bienvenido 
# martes 16, hasta ahora dejare la estructura del menu, al siguiente dia actualizare el menu semi funcional :p
# miercoles 17, implemente la opcion 1 y 2 funcionales 
# Jueves 18: implementamos la opcion 3 jeje
# viernes 19: finalmente se implemento la opcion 4 para borrar una tarea jejeje

lista_tareas = []

# aqui cree la funcion que mostrara el menu 
def mostrar_menu():
    print("\n--- SISTEMA DE TAREAS PERSONALES ---")
    print("1. Agregar tarea")
    print("2. mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir del sistema")
     
  # funcion que sirve para registrar tareas 
def agregar_tarea():
    print("\n--- Agregar Tarea ---")
    nombre_tarea = input("Ingrese el nombre de la tarea: ").strip()
    
    if nombre_tarea == "":
        print("Error: El nombre de la tarea no puede estar vacío")
        return

    nueva_tarea = {"nombre": nombre_tarea, "estado": "Pendiente"} 
    lista_tareas.append(nueva_tarea)
    print(f" Tarea '{nombre_tarea}' agregada con éxito.")

# funcion para eliminar tareas jejeje
def eliminar_tarea():
    print("\n--- eliminar tarea ---")

    if len(lista_tareas) == 0:
        print("No hay tareas disponibles para eliminar.")
        return
    
    listar_tareas()

    try:
        opcion_id = input("\nIngrese el número de la tarea que desea eliminar: ").strip()
        indice = int(opcion_id) - 1 
        if indice < 0 or indice >= len(lista_tareas):
            print("Error: El número de tarea no existe en el sistema.")
            return
        
        tarea_eliminada = lista_tareas.pop(indice)
        print(f" La tarea '{tarea_eliminada['nombre']}' ha sido eliminada con éxito.")

    except ValueError:
        print("Error: Debe ingresar un número entero positivo válido.")


# pa mostrar tareas registradas
def listar_tareas():
    print("\n--- Lista de tareas ---")
    if len(lista_tareas) == 0:
        print("No hay tareas registradas")
        return False 
    
    for i in range(len(lista_tareas)):
        tarea = lista_tareas[i]
        print(f"{i + 1}. [{tarea['estado']}] {tarea['nombre']}")
    return True

def completar_tarea():
    print("\n--- Marcar Tarea como Completada ---")

    if len(lista_tareas) == 0:
        print("No hay tareas guardadas para modificar.")
        return
    listar_tareas()

    try:
        opcion_id = input("\nIngrese el número de la tarea que desea completar: ").strip()
        indice = int(opcion_id) - 1 
        if indice < 0 or indice >= len(lista_tareas):
            print("Error: El número de tarea no existe en el sistema.")
            return
        
        lista_tareas[indice]["estado"] = "Completada"
        print(f" Genial! La tarea '{lista_tareas[indice]['nombre']}' ahora está Completada.")
        
    except ValueError:
        print("Error: Debe ingresar un número entero positivo válido.")

# mientras hacia el programa descubri que para hacer un bucle mas basico con funciones
# usar continuar y agregar True y false es mas practico como ahora
def iniciar_programa():
    continuar = True
    
    #como continuar es true llamara a la funcion que mostrara el menu y luego pedira al usuario que ingrese una opcion
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("\n¡Gracias por utilizar el sistema!")
            print("Saliendo del programa")
            continuar = False
            #el false es como el break en este caso, quede plop 
        else:
            print("\n Opción no válida. Por favor, ingrese un número entero positivo del 1 al 5")

if __name__ == "__main__":
    iniciar_programa()
