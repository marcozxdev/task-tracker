

# modulos necesarios para funcionar
import json # donde se van a almacenar los datos 
import os # para la ruta de el archivo json



# funciones que simulan los comandos en la terminal
def add(args): # add para añadir tareas 
    #print("\n".join(args))


def mark_done(args): # mark_done para marcar como hecho
    pass


def mark_in_progress(args): # mark_in_progres para marcar como en progreso 
    pass


def list(): # list lista todas las tareas
    pass


def list_done(): # list_done lista todas las tareas que estan hechas 
    pass


def list_in_progress(): # lis__in_progres lista las tareas que  estan en progreso
    pass


# comandos existentes van de la mano con las funciones 
commands = {
    "add": add,
    "mark-done": mark_done,
    "mark-progress": mark_in_progress,
    "list": list,
    "list-done": list_done,
    "list-in-progress": list_in_progress
}


# menu donde el usuario interactua con la terminal
def menu():

    while True:    
        print("Bienvenido a Task Traker")
        print("Que desea hacer?")
        print("add <task>")
        print("mark-done <ID>")
        print("mark-in-progress <ID>")
        print("list")
        print("list-done")
        print("list-in-progress")
        print("exit\n")

        opc = input('task-cli ') # entrad de los comandos
        

        if not opc:
            print("please write")
            continue

        if opc == "exit":
            print("bye...")
            break

      # logica de ejecutar comandos
        parts = opc.split() # divido la entrada por espacio y lo almaceno como una lista

        if not parts: # si no hay partes no se ejecuta lo de abajo
            continue

        comando = parts[0]  # almaceno la primera palabra en este caso el comando
        arguments = parts[1:] # el resto de la entrada se podria tomar como parametro 
      
        if comando == "exit":
            print("bye...")
            break
        if comando in commands:
            commands[comando](arguments) # acede al dicionaro donde estan los comandos junto con las funciones como valor y las ejecuta y les da parametros si lo nesesitan
        else:
            print("error command ") # lanza error en caso de que no exista el comando 











menu() # se llama la funcion menu para iniciar el programa































