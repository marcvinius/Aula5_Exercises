# Programa para calcular o bônus dos cavaleiros

# Solicita o número de missões completadas
missões_completadas = int(input("Digite o número de missões completadas pelo cavaleiro: "))

# Determina o valor do bônus com base no número de missões
if missões_completadas > 10:
    bônus = 100
elif 5 <= missões_completadas <= 10:
    bônus = 50
else:
    bônus = 10

# Exibe o valor do bônus
print(f"O bônus do cavaleiro é: {bônus} moedas de ouro.")
