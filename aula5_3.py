# Programa para adivinhar o animal favorito

# Pergunta ao usuário se o animal favorito é mamífero ou réptil
tipo_animal = input("Seu animal favorito é mamífero ou réptil? (m/r): ").strip().lower()

# Sugestão com base na resposta
if tipo_animal == 'm':
    print("Seu animal favorito é um cachorro!")
elif tipo_animal == 'r':
    print("Seu animal favorito é uma tartaruga!")
else:
    print("Opção inválida! Por favor, responda com 'm' para mamífero ou 'r' para réptil.")
