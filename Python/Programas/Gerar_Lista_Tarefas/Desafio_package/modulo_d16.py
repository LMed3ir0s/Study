import copy

list_tasks = []
list_undo = []
list_redo = []

def imprimir_lista(lista, title):
    if not lista:
        print('⚠️ Lista está vazia.')
        return
    
    print(title)
    for i, task in enumerate(lista, start=1):
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
@decorator_factory()
def task_add(param):
    list_undo.append(copy.deepcopy(list_tasks))
    list_tasks.append(param)
    list_redo.clear()
    print(f'\n✅ | Tarefa "{param}" adicionada com sucesso!')
    imprimir_lista(list_tasks,'\n📋 | Lista de Tarefas:')

#Desfazer   
@decorator_factory()
def task_undo(_=None):
    if not list_undo:
        print("⚠️ | Nada para desfazer.")
        return
    list_redo.append(copy.deepcopy(list_tasks))
    last_state = list_undo.pop()
    list_tasks.clear()
    list_tasks.extend(last_state)
    print(f'\n↩️ | Tarefa desfeita!')
    imprimir_lista(list_tasks, '\n📋 | Lista atualizada:')
    

#Refazer
@decorator_factory()
def task_redo(_=None):
    if not list_redo:
        print("⚠️ | Nada para Refazer.")
        return
    list_undo.append(copy.deepcopy(list_tasks))
    next_state = list_redo.pop()
    list_tasks.clear()
    list_tasks.extend(next_state)
    print(f'\n↪️ | Tarefa refeita!')
    imprimir_lista(list_tasks, '\n📋 | Lista atualizada:')