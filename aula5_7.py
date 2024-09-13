# Programa para classificar a altura de uma planta

# Recebe a altura da planta em metros
altura_planta = float(input("Digite a altura da planta em metros: "))

# Classifica a planta com base na altura
if altura_planta < 1:
    classificacao = "pequena"
elif 1 <= altura_planta <= 3:
    classificacao = "média"
else:
    classificacao = "grande"

# Exibe a classificação da planta
print(f"A planta é classificada como {classificacao}.")

