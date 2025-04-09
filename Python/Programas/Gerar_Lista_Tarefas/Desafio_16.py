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

import os
from Desafio_package import (
    task_add, task_undo, task_redo
    )

list_tasks = []
list_undo = []
list_redo = []


while True:

    user_input = input(
        '\nVocê deseja:\n'
        ' [a]dicionar\n'
        ' [d]esfazer\n'
        ' [r]efazer\n'
        ' [s]air\n'
        ' Digite sua opção: '
        ).strip().lower()

    if user_input not in ('a','d','r','s'):
        print('❌ | Você não digitou opção válida.')
        continue

    if user_input.startswith('a'):
        # os.system('cls')
        add = input(f'Digite a tarefa que você deseja adicionar:')
        task_add(str(add))
        continue

    if user_input.startswith('d'):
        # os.system('cls')
        task_undo()
        continue

    if user_input.startswith('r'):
        # os.system('cls')
        task_redo()
        continue

    if user_input.startswith('s'):
        print('👋 | Saindo do programa. Até logo!')
        break

    
