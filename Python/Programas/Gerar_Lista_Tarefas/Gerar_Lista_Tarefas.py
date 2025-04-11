# Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


#################################################################################

#lista para armazenar
#input com acao
#tratamento de erro
#limpar
#adicionar
#remover
#desfazer
#refazer

#################################################################################

from colorama import init, Fore, Style
import os
from Modulo_package import (
    task_add, task_undo, task_redo, task_remove, task_edit, list_tasks, imprimir_lista,
    load_tasks
    )
init(autoreset=True)
load_tasks()



while True:

    user_input = input(
        '\nVocê deseja:\n'
        ' [1]adicionar\n'
        ' [2]desfazer\n'
        ' [3]refazer\n'
        ' [4]alterar tarefa especifica\n'
        ' [5]remover tarefa especifica\n'
        ' [6]sair\n'
        ' Digite sua opção: '
        ).strip().lower()

    if user_input not in ('1','2','3','4','5', '6'):
        print(f'{Fore.LIGHTRED_EX}❌ | Você não digitou opção válida.{Style.RESET_ALL}')
        continue

    if user_input.startswith('1'):
        os.system('cls')
        print(f'{Fore.LIGHTYELLOW_EX}⭐️ | Adicionar{Style.RESET_ALL}')
        add = input(f'{Fore.YELLOW}Digite a tarefa que você deseja adicionar:{Style.RESET_ALL}')
        task_add(str(add))
        continue

    if user_input.startswith('2'):
        os.system('cls')
        print(f'{Fore.LIGHTYELLOW_EX}⭐️ | Desfazer{Style.RESET_ALL}')
        task_undo()
        continue

    if user_input.startswith('3'):
        os.system('cls')
        print(f'{Fore.LIGHTYELLOW_EX}⭐️ | Refazer{Style.RESET_ALL}')
        task_redo()
        continue

    if user_input.startswith('4'):
        os.system('cls')
        print(f'{Fore.LIGHTYELLOW_EX}⭐️ | Editar Tarefa Especifica\n{Style.RESET_ALL}')
        imprimir_lista(list_tasks, 'Lista de Tarefas:')
        index = input(f'\n{Fore.YELLOW}Escolha o numero da Tarefa que deseja alterar:{Style.RESET_ALL}')
        param = input(f'\n{Fore.YELLOW}Digite a nova Tarefa:{Style.RESET_ALL}')
        task_edit(index,param)
        continue

    if user_input.startswith('5'):
        os.system('cls')
        print(f'{Fore.LIGHTYELLOW_EX}⭐️ | Remover Tarefa Especifica{Style.RESET_ALL}\n')
        imprimir_lista(list_tasks, 'Lista de Tarefas:')
        index = input(f'\n{Fore.YELLOW}Escolha o numero da Tarefa que deseja remover:{Style.RESET_ALL}')
        task_remove(index)
        continue

    if user_input.startswith('6'):
        os.system('cls')
        print(f'{Fore.LIGHTYELLOW_EX}⭐️ | Sair{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}👋 | Saindo do programa. Até logo!{Style.RESET_ALL}')
        break
