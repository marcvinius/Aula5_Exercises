# Programa para ativar ou desativar o sistema de defesa do castelo mágico

# Solicita a posição do exército
posicao = input("Digite a posição do exército (dentro ou fora do castelo): ").strip().lower()

# Usa match-case para ativar ou desativar o sistema de defesa
match posicao:
    case "dentro":
        print("O sistema de defesa está desativado.")
    case "fora":
        print("O sistema de defesa está ativado.")
    case _:
        print("Posição inválida! Por favor, digite 'dentro' ou 'fora'.")