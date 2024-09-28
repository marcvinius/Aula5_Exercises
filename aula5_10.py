# Programa para escolher um desafio

# Solicita a escolha do número da porta
porta = int(input("Escolha uma porta (1 a 5): "))

# Usa match-case para exibir o desafio correspondente
match porta:
    case 1:
        print("Atrás da porta 1, você enfrentará um dragão feroz!")
    case 2:
        print("Atrás da porta 2, você encontrará um labirinto cheio de armadilhas!")
    case 3:
        print("Atrás da porta 3, um enigma que desafiará sua inteligência!")
    case 4:
        print("Atrás da porta 4, você encontrará uma tempestade de monstros!")
    case 5:
        print("Atrás da porta 5, um tesouro guardado por um guardião misterioso!")
    case _:
        print("Escolha inválida! Por favor, escolha um número entre 1 e 5.")
