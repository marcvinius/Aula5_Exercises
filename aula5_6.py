# Programa para comparar a velocidade de dois dragões

# Função para calcular a velocidade
def calcular_velocidade(distancia, tempo):
    return distancia / tempo

# Recebe a distância e o tempo do primeiro dragão
distancia_dragao1 = float(input("Digite a distância percorrida pelo primeiro dragão (em metros): "))
tempo_dragao1 = float(input("Digite o tempo gasto pelo primeiro dragão (em segundos): "))

# Recebe a distância e o tempo do segundo dragão
distancia_dragao2 = float(input("Digite a distância percorrida pelo segundo dragão (em metros): "))
tempo_dragao2 = float(input("Digite o tempo gasto pelo segundo dragão (em segundos): "))

# Calcula a velocidade de cada dragão
velocidade_dragao1 = calcular_velocidade(distancia_dragao1, tempo_dragao1)
velocidade_dragao2 = calcular_velocidade(distancia_dragao2, tempo_dragao2)

# Compara as velocidades e exibe o resultado
if velocidade_dragao1 > velocidade_dragao2:
    print("O primeiro dragão é mais rápido.")
elif velocidade_dragao1 < velocidade_dragao2:
    print("O segundo dragão é mais rápido.")
else:
    print("Ambos os dragões têm a mesma velocidade.")
