# if (se) / elif (se não se) / else (se não)

entrada = input('Você quer "Entrar" ou "Sair" do sistema? ')

if entrada == 'Entrar':
    print('Você entrou no Sistema.')

elif entrada == 'Sair':
    print('Você saiu do Sistema.')

else:
    print('Você não digitou "Entrar" ou "Sair".')

print('FORA DO BLOCO')