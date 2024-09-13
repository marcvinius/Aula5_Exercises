moedas_de_1_real = int(input("Digite a quantidade de moedas de 1 real:"))
moedas_de_50_centavos = int(input("Digite a quantidade de moedas de 50 centavos:"))
moedas_de_25_centavos = int(input("Digite a quantidade de moedas de 25 centavos:"))

valor_total_real = moedas_de_1_real * 1.00
valor_total_50_centavos = moedas_de_50_centavos * 0.50
valor_total_25_centavos = moedas_de_25_centavos * 0.25

valor_total = valor_total_real + valor_total_50_centavos + valor_total_25_centavos

print(f"O valor total das moedas é: R${valor_total:.2f}")