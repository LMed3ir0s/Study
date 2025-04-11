import json
import copy
import os
from colorama import init, Fore, Style

init(autoreset=True)

GL_JSON = 'tasks.json'

def save_tasks():
    with open(GL_JSON, 'w', encoding='utf-8') as f:
        json.dump(list_tasks, f, ensure_ascii=False, indent=4)


def load_tasks():
    if os.path.exists(GL_JSON):
        with open (GL_JSON, 'r', encoding='utf-8') as f:
            try:
                tasks = json.load(f)
                list_tasks.clear()
                list_tasks.extend(tasks)
            except json.JSONDecodeError:
                print(f'{Fore.LIGHTYELLOW_EX}⚠️ | Arquivo JSON está vazio ou corrompido.')




list_tasks = []
list_undo = []
list_redo = []

def imprimir_lista(lista, title):
    if not lista:
        print(f'{Fore.LIGHTYELLOW_EX}⚠️ Lista está vazia.')
        return
    
    print(f'{Fore.CYAN}{title}{Style.RESET_ALL}')
    for i, task in enumerate(lista, start=1):
        print(f'{Fore.BLUE}{i}. {task}{Style.RESET_ALL}')

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
    print(f'\n{Fore.LIGHTGREEN_EX}✅ | Tarefa "{param}" adicionada com sucesso!')
    imprimir_lista(list_tasks,'\n📋 | Lista de Tarefas:')
    save_tasks()

#Desfazer   
@decorator_factory()
def task_undo(_=None):
    if not list_undo:
        print(f"{Fore.LIGHTYELLOW_EX}⚠️ | Nada para desfazer.")
        return
    list_redo.append(copy.deepcopy(list_tasks))
    last_state = list_undo.pop()
    list_tasks.clear()
    list_tasks.extend(last_state)
    print(f'\n{Fore.LIGHTMAGENTA_EX}↩️ | Tarefa desfeita!')
    imprimir_lista(list_tasks, '\n📋 | Lista atualizada:')
    save_tasks()

#Refazer
@decorator_factory()
def task_redo(_=None):
    if not list_redo:
        print(f"{Fore.LIGHTYELLOW_EX}⚠️ | Nada para Refazer.")
        return
    list_undo.append(copy.deepcopy(list_tasks))
    next_state = list_redo.pop()
    list_tasks.clear()
    list_tasks.extend(next_state)
    print(f'\n{Fore.LIGHTMAGENTA_EX}↪️ | Tarefa refeita!')
    imprimir_lista(list_tasks, '\n📋 | Lista atualizada:')
    save_tasks()

#Remover tarefa específica
@decorator_factory()
def task_remove(index):
    try:
        index = int(index) - 1
        if index < 0 or index >= len(list_tasks):
            print()
            return
        list_undo.append(copy.deepcopy(list_tasks))
        list_redo.clear()
        task_removida = list_tasks.pop(index)
        print(f'🗑️\n{Fore.LIGHTMAGENTA_EX}Tarefa "{task_removida}" removida com sucesso.\n')
        imprimir_lista(list_tasks, '\n📋 | Lista atualizada:')
        save_tasks()
    except ValueError:
        print(f'{Fore.LIGHTRED_EX}❌ | Por favor, digite um número válido.')

@decorator_factory()
def task_edit(index, param):
    try:
        index = int(index) - 1
        if index < 0 or index >= len(list_tasks):
            print(f'{Fore.LIGHTRED_EX}❌ Índice inválido.')
            return         
        list_undo.append(copy.deepcopy(list_tasks))
        list_redo.clear()
        task_antiga = list_tasks[index]
        list_tasks[index] = param
        print(f'{Fore.LIGHTMAGENTA_EX}✏️ | Tarefa "{task_antiga}", atualizada para "{param}."\n')
        imprimir_lista(list_tasks, '\n📋 | Lista atualizada:')
        save_tasks()
    except ValueError:
        print(f'{Fore.LIGHTRED_EX}❌ | Por favor, digite um número válido.')
