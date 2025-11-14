

# modulos necesarios para funcionar
import json # donde se van a almacenar los datos 
import os # para la ruta de el archivo json
# import datetime # depronto mas adelanete la use para guardar fechas
import time


DATA_TASK = "task-traker-cli/data/tasks.json"

def ensure_file(file):
    if not os.path.exists(file):  # creamos el archivo si no existe
            with open(file, "w") as f:
                json.dump([], f, indent=4)


def load(file): # carga los datos que esten en el file
    ensure_file(file)
    with open(file, "r") as f:
        return json.load(f)

def save(path, data): # guarda los datos en  el archivo
    with open(path, "w") as f: 
        json.dump(data, f, indent=4)

# cargamos los datos 
tasks: list = load(DATA_TASK)


# funciones que simulan los comandos en la terminal
def add(args): # add para añadir tareas 
    # print(" ".join(args))
    
    # añado un diccionario en la lista para simular un a bases de datos 
    
    tasks.append({"ID": int(len(tasks)+1),"task": " ".join(args), "isdone": False})
    print(f"added task: ID: {len(tasks)}  task: {' '.join(args)}")
    save(DATA_TASK, tasks)
    


def mark_done(args): # mark_done para marcar como hecho

    # valida que aya argumentos
    if not args:
        print("please write id")
        return
    
    # solo usa el primer argumento para que no aya bugs
    idtask = args[0]
    try:
        int(idtask)
    except:
        print("just write numbers")
        return

    # logica de busqueda y marcado de tarea
    for i in tasks:

        if int(idtask) == i["ID"]: # valida que tenga el mismo id 
            i["isdone"] = True # cambia el valor de la tarea                                    
            print(f"ID: {i['ID']} task: {i['task']} mark: [DONE]\n")
            # guardamos los datos
            save(DATA_TASK, tasks)
            return 
    else:
        print("it's task not exist  ")


def delete_task(args):
    try:
        if not args:
            print("please write ID")
            return
        
        idtask = int(args[0])
        
        for i in tasks:

            if idtask == i["ID"]: # valida que tenga el mismo id 
                tasks.remove(i) # borra la tarea
                print(f"ID: {i['ID']} task: {i['task']}  [delete] \n")
                # se guardan los datos
                save(DATA_TASK, tasks)
                return 

        
    except:
        print("just write numbers")


# esta funcion tiene polimorfismo ya que se puede comportar diferente dependiendo de los argumentos dados
def list(isdone= "done" or "progress" ): # list lista todas las tareas
    


    # valida los argumontos para que no haya bugs si se da un argumento como done o progress
    if not isdone == "done" and not isdone == "progress" and  isdone:
        print("\nerror command")
        return
    
    #valida que haya tareas en la lista 
    if not tasks:
        print("no tasks, please add tasks")
        return

    # logica de mostrar las tareas que estan terminadas
    if isdone == "done"  or not isdone:
        print("\nDONE: \n")
        for i in tasks:
            if i["isdone"] == True:
                print(i["ID"], i["task"], "[DONE]")
    

    # logica para mostrar las tareas que estan en progreso
    if isdone == "progress" or not isdone :
        print("\nIN PROGRESS: \n")
        for i in tasks:
            if i["isdone"] == False:
                print(i["ID"], i["task"], "[IN PROGRESS]")
    
    print()


def list_done(none): # list_done lista todas las tareas que estan hechas 
    list("done") # se llama a list("done") para que liste solo las tareas que estan hechas


def list_in_progress(none): # lis__in_progres lista las tareas que  estan en progreso
    list("progress") # se llama a list("progress") solo lista las tareas que estan en progreso


# comandos existentes van de la mano con las funciones 
commands = {
    "add": add,
    "mark-done": mark_done,
    "delete": delete_task,
    "list": list,
    "list-done": list_done,
    "list-in-progress": list_in_progress
}


# menu donde el usuario interactua con la terminal
def menu():

    while True:    
        print("\nTask Traker!\n")
        print("add <task>")
        print("mark-done <ID>")
        print("delete <ID>")
        print("list")
        print("list-done")
        print("list-in-progress")
        print("exit\n")

        opc = input('task-cli ') # entrad de los comandos
        print()

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
            return
            
        if comando in commands:
            commands[comando](arguments) # acede al dicionaro donde estan los comandos junto con las funciones como valor y las ejecuta y les da parametros si lo nesesitan
        else:
            print("error command ") # lanza error en caso de que no exista el comando 











menu() # se llama la funcion menu para iniciar el programa































