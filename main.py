print("Bienvenido al Sistema de Tareas Personales")

def mostrar_menu():
    print("\n--- SISTEMA DE TAREAS PERSONALES ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir del sistema")
    print("======================================")

def iniciar_programa():
  continuar = True

while continuar:
  mostrar_menu()
  opcion = input("eliga una opcion 1-5"\n>>)
  
