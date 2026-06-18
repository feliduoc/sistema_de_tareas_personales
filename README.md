# Sistema de Registro de Tareas Personales :D
Este proyecto es una aplicación interactiva en consola desarrollada en Python para la asignatura de **Fundamentos de Programación**. Permite gestionar de manera eficiente tareas diarias

---

## funciones del programa
El programa cumple con las siguientes operaciones integradas:
1. **Agregar tareas** con estado inicial "Pendiente"
2. **Listar tareas registradas** de forma ordenada
3. **Marcar tareas como completadas** modificando su estado interno
4. **Eliminar tareas** del registro general (en desarrollo)
5. **Salir del sistema** asegurando un cierre limpio del bucle principal

---

## Componentes Utilizados
El código fue diseñado bajo los estándares evaluados en el curso, aplicando:
* **Estructura de Datos:** Lista de diccionarios para el almacenamiento dinámico
* **Ciclos y Control:** Uso de bucles `while` para la persistencia del menú y ciclos `for` con `range(len())` para el recorrido de datos
* **Manejo de Excepciones:** Bloques `try - except ValueError` para la validación robusta de entradas del usuario sin interrupciones del programa
* **Modularidad:** Funciones específicas para separar las responsabilidades del sistema

---

## Cómo Ejecutar el Programa
1. Asegúrate de tener instalado **Python 3,14**
2. Descarga el archivo principal del repositorio: `main.py`
3. Abre tu terminal o consola de comandos en la carpeta del archivo
4. Ejecuta el siguiente comando:
   ```bash
   python main.py
