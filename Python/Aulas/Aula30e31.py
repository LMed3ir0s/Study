"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 62  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega


# if velocidade > RADAR_1:
#     print(
#         'A velocidade do carro ultrapassou a velocidade permitida pelo Radar 1.'
#     )

# if local_carro >= (LOCAL_1 - RADAR_RANGE) and\
#     local_carro <= (LOCAL_1 + RADAR_RANGE) and\
#     velocidade > RADAR_1:
#         print ('Carro multado em Radar 1.')

Velocidade_Carro_Ultrapassou_RADAR_1 = velocidade > RADAR_1
Carro_passou_RADAR_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = Carro_passou_RADAR_1 and Velocidade_Carro_Ultrapassou_RADAR_1

if Velocidade_Carro_Ultrapassou_RADAR_1:
    print('Velocidade do carro ultrapassou a velocidade permitida pelo radar 1')

if Carro_passou_RADAR_1:
    print('Carro pelo passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')