print("--- Bienvenido al Sistema de Tareas Personales :D ---")

lista_tareas = []

# aqui cree la funcion que mostrara el menu
def mostrar_menu():
    print("\n--- SISTEMA DE TAREAS PERSONALES ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir del sistema")
     
  #variable que sirve para registrar tareas 
def agregar_tarea():
    print("\n--- Agregar Tarea ---")
    nombre_tarea = input("Ingrese el nombre de la tarea: ").strip()
    
    if nombre_tarea == "":
        print(" Error: El nombre de la tarea no puede estar vacío")
        return

    nueva_tarea = {"nombre": nombre_tarea, "estado": "Pendiente"} 
    lista_tareas.append(nueva_tarea)
    print(f" Tarea '{nombre_tarea}' agregada con éxito.")

#pa mostrar tareas registradas
def listar_tareas():
    print("\n--- Lista de tareas ---")
    if len(lista_tareas) == 0:
        print("No hay tareas registradas")
        return
    
    for i in range(len(lista_tareas)):
        tarea = lista_tareas[i]
        print(f"{i + 1}. [{tarea['estado']}] {tarea['nombre']}")


# mientras hacia el programa descubri que para hacer un bucle mas basico con funciones
# usar continuar y agregar True y false es mas practico como ahora
def iniciar_programa():
    continuar = True
    
    #como continuar es true llamara a la funcion que mostrara el menu y luego pedira al usuario que ingrese una opcion, dependiendo de la opcion se llamara a la funcion correspondiente, si el usuario ingresa 5 se cambiara continuar a False y el programa terminara, si el usuario ingresa una opcion no valida se mostrara un mensaje de error y el menu se mostrara nuevamente
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        # hasta ahora dejare la estructura del menu, al siguiente dia actualizare el menu semi funcional :p
        #miercoles 17, implemente la opcion 1 y 2 funcionales 

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            print("\n[en desarrollo] Aquí se marcarán las tareas como completadas")
        elif opcion == "4":
            print("\n[en desarrollo] Aquí se eliminarán las tareas")
        elif opcion == "5":
            print("\n¡Gracias por utilizar el sistema!")
            print("Saliendo del programa")
            continuar = False
            #el false es como el break en este caso, quede plop 
        else:
            print("\n Opción no válida. Por favor, ingrese un número entero positivo del 1 al 5")

# Bloque principal para ejecutar el programa
if __name__ == "__main__":
    iniciar_programa()
