# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:',pergunta['Pergunta'])

    
    opcoes = pergunta['Opções']
    for i,opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')
        
    int_escolha = None
    acertou = False
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        int_escolha = int(escolha)

        if int_escolha is not None:
            if int_escolha >= 0 and int_escolha < qtd_opcoes:
                if opcoes[int_escolha] == pergunta['Resposta']:
                    acertou = True
                    

    if acertou:
            print('Certa resposta!')
            qtd_acertos += 1
    else:
            print('Resposta incorreta.')

print('Você acertou ', qtd_acertos)
print('de ', len(perguntas), 'perguntas.')