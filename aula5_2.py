# Recebe a quantidade de ferro e ouro em kg
ferro = float(input("Digite a quantidade de ferro em kg: "))
ouro = float(input("Digite a quantidade de ouro em kg: "))

# Calcule o total de metal
total_metal = ferro + ouro

# Verifica se o total de metal é zero para evitar divisão por zero
if total_metal == 0:
    print("A quantidade total de metal não pode ser zero.")
else:
    # Calcula a porcentagem de ferro na liga
    porcentagem_ferro = (ferro / total_metal) * 100

    # Verifica se a porcentagem de ferro é suficiente
    if porcentagem_ferro >= 70:
        print(f"A porcentagem de ferro na liga é suficiente: {porcentagem_ferro:.2f}%")
    else:
        print(f"A porcentagem de ferro na liga é insuficiente: {porcentagem_ferro:.2f}%")
