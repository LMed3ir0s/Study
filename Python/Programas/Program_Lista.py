'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.

'''
import os
lista = []

while True:

    entrada = input('Você deseja [i]nserir [a]pagar [l]istar: ').lower()
    
    
    if entrada == 'i':
        adicionar = input('O que você deseja adicionar?: ')
        lista.append(adicionar)
        os.system('cls')
        continue

    elif entrada == 'l':
        os.system('cls')
        if len(lista) == 0:
                print('A lista está vazia.')
        for i, adicionar in enumerate(lista):
                print(i, adicionar)        
        continue

    elif entrada == 'a':
        for i, adicionar in enumerate(lista):
            print(i, adicionar)

        try:
            indice_apagar = input('Digite o numero do item da lista que você deseja apagar: ')
            str_apagar = str(indice_apagar)
            int_apagar = int(str_apagar)
            lista.pop(int_apagar)
            print('item apagado da lista. \n'
                  'Segue Lista atualizada:')
            for i, adicionar in enumerate(lista):
                print(i, adicionar)
            
        except IndexError:
            print('Você digitou um número inválido')
        except ValueError:
            print('Você digitou um número inválido')
        
        continue

    else:
        print('Por favor digite apenas "i", "l" ou "a".')
        continue