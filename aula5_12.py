# Programa para escolher a arma mais adequada para o herói

# Função para verificar se a arma é adequada
def arma_adequada(poder_ataque, durabilidade):
    return poder_ataque > 50 and durabilidade > 70

# Solicita os valores das armas
print("Digite os valores das armas:")

# Arma 1
poder_ataque1 = float(input("Espada - Poder de ataque: "))
durabilidade1 = float(input("Espada - Durabilidade: "))

# Arma 2
poder_ataque2 = float(input("Arco - Poder de ataque: "))
durabilidade2 = float(input("Arco - Durabilidade: "))

# Arma 3
poder_ataque3 = float(input("Lança - Poder de ataque: "))
durabilidade3 = float(input("Lança - Durabilidade: "))

# Verifica a adequação de cada arma
adequada1 = arma_adequada(poder_ataque1, durabilidade1)
adequada2 = arma_adequada(poder_ataque2, durabilidade2)
adequada3 = arma_adequada(poder_ataque3, durabilidade3)

# Determina a melhor arma
if adequada1 and not (adequada2 or adequada3):
    print("A arma mais adequada é a Espada!")
elif adequada2 and not (adequada1 or adequada3):
    print("A arma mais adequada é o Arco!")
elif adequada3 and not (adequada1 or adequada2):
    print("A arma mais adequada é a Lança!")
elif adequada1 and adequada2 and not adequada3:
    print("As armas mais adequadas são a Espada e o Arco!")
elif adequada1 and adequada3 and not adequada2:
    print("As armas mais adequadas são a Espada e a Lança!")
elif adequada2 and adequada3 and not adequada1:
    print("As armas mais adequadas são o Arco e a Lança!")
elif adequada1 and adequada2 and adequada3:
    print("Todas as armas são adequadas!")
else:
    print("Nenhuma arma é adequada. Busque uma nova arma!")
