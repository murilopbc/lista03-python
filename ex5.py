divida = int(input("Digite o valor da sua dívida: "))
saldo = int(input("Digite o valor dísponivel na sua conta: "))

valor_atual = saldo - divida
if valor_atual < 0:
    print("Você está com o saldo negativo, devendo", valor_atual, "reais")
else:
    print("Você está com o saldo positivo com ", valor_atual, "reais dísponivel na sua conta")
