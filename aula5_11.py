# Programa para determinar o próximo governante baseado nas médias dos candidatos

# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Solicita as notas dos três candidatos
candidato1_notas = list(map(float, input("Digite as notas do Candidato 1 (separadas por espaço): ").split()))
candidato2_notas = list(map(float, input("Digite as notas do Candidato 2 (separadas por espaço): ").split()))
candidato3_notas = list(map(float, input("Digite as notas do Candidato 3 (separadas por espaço): ").split()))

# Calcula as médias
media1 = calcular_media(candidato1_notas)
media2 = calcular_media(candidato2_notas)
media3 = calcular_media(candidato3_notas)

# Exibe as médias
print(f"Média do Candidato 1: {media1:.2f}")
print(f"Média do Candidato 2: {media2:.2f}")
print(f"Média do Candidato 3: {media3:.2f}")

# Determina o candidato com a maior média ou verifica empate
if media1 > media2 and media1 > media3:
    print("O Candidato 1 é o próximo governante!")
elif media2 > media1 and media2 > media3:
    print("O Candidato 2 é o próximo governante!")
elif media3 > media1 and media3 > media2:
    print("O Candidato 3 é o próximo governante!")
else:
    print("Houve um empate entre os candidatos.")
