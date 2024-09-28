# Programa para verificar se o portal de viagem no tempo pode ser ativado

# Solicita os parâmetros
energia = float(input("Digite o nível de energia (%): "))
coordenadas = input("As coordenadas de destino estão corretas? (sim/não): ").strip().lower()
tempo = float(input("Digite o tempo ajustado (em segundos): "))

# Verifica se todos os parâmetros estão corretos
energia_correta = energia > 80
coordenadas_certas = coordenadas == "sim"
tempo_correto = tempo > 0

# Avalia a ativação do portal
if energia_correta and coordenadas_certas and tempo_correto:
    print("Portal ativado com sucesso!")
else:
    if not energia_correta:
        print("Problema: Energia abaixo de 80%.")
    if not coordenadas_certas:
        print("Problema: Coordenadas de destino incorretas.")
    if not tempo_correto:
        print("Problema: Tempo ajustado incorretamente.")