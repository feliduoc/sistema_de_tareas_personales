print("Bienvenido al Sistema de Tareas Personales")
# aqui cree la funcion que mostrara el menu
def mostrar_menu():
    print("\n--- SISTEMA DE TAREAS PERSONALES ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir del sistema")

# mientras hacia el programa descubri que para hacer un bucle mas basico con funciones
# usar continuar y agregar True y false es mas practico como ahora
def iniciar_programa():
    continuar = True

    #como continuar es true llamara a la funcion que mostrara el menu
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        # hasta ahora dejare la estructura del menu, al siguiente dia actualizare el menu semi funcional :p
        if opcion == "1":
            print("\n[en desarrollo] Aquí se agregarán las tareas")
        elif opcion == "2":
            print("\n[en desarrollo] Aquí se listarán las tareas")
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

#sin esto el programa no se muestra, lol
if __name__ == "__main__":
    iniciar_programa()
