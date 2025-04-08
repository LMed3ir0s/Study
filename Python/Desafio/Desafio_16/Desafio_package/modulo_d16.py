import copy

list_tasks = []
list_undo = []
list_redo = []

def imprimir_lista(list, title):
    if not list:
        print('Lista está vazia.')
        return
    
    print(title)
    for i, task in enumerate(list, start=1):
        print(f'{i}. {task}')

#Função decoradora
def decorator_factory(a=None):
    def funct_factory(funct):
        def nested(*args, **kwargs):
            result = funct(*args, **kwargs)
            return result
        return nested
    return funct_factory


#Criar task
@decorator_factory
def task_add(param):
    list_undo.append(copy.deepcopy(list_tasks))
    list_tasks.append(param)
    list_redo.clear()
    return [
        print(f'Tarefa {param} adicionada à Lista:')
    ]

#Desfazer   
@decorator_factory
def task_undo(_=None):
    if not list_undo:
        print("Nada para desfazer.")
        return
    list_redo.append(copy.deepcopy(list_tasks))
    last_state = list_undo.pop()
    list_tasks.clear()
    list_tasks.extend(last_state)
    print(f'Tarefa Desfeita!\n')
    imprimir_lista(list_tasks, 'Lista atual:')
    

#Refazer
@decorator_factory
def task_redo(_=None):
    ...
    return [
        print(f'Tarefa {param} Refeita.')
    ]
