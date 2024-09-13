# Programa para verificar se a quantidade de água é suficiente para chegar ao oásis

# Recebe a quantidade de água disponível e a distância até o oásis
agua_disponivel = float(input("Digite a quantidade de água disponível em litros: "))
distancia_ate_oasis = float(input("Digite a distância até o oásis em quilômetros: "))

# Calcula a quantidade de água necessária
agua_necessaria = distancia_ate_oasis * 2

# Verifica se a água disponível é suficiente
if agua_disponivel >= agua_necessaria:
    print("A quantidade de água é suficiente para chegar ao oásis.")
else:
    print("A quantidade de água não é suficiente para chegar ao oásis.")
