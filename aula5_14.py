# Programa para julgar o duelo entre dois guerreiros

# Solicita as habilidades do Guerreiro 1
ataque1 = float(input("Guerreiro 1 - Poder de ataque: "))
defesa1 = float(input("Guerreiro 1 - Poder de defesa: "))

# Solicita as habilidades do Guerreiro 2
ataque2 = float(input("Guerreiro 2 - Poder de ataque: "))
defesa2 = float(input("Guerreiro 2 - Poder de defesa: "))

# Calcula a soma de ataque e defesa para cada guerreiro
soma1 = ataque1 + defesa1
soma2 = ataque2 + defesa2

# Determina o vencedor
if soma1 > soma2:
    print("O Guerreiro 1 é o vencedor!")
elif soma2 > soma1:
    print("O Guerreiro 2 é o vencedor!")
else:  # Empate
    if defesa1 > defesa2:
        print("O Guerreiro 1 é o vencedor por defesa!")
    elif defesa2 > defesa1:
        print("O Guerreiro 2 é o vencedor por defesa!")
    else:
        print("Houve um empate total!")

