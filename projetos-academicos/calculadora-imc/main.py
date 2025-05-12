def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = calcular_imc(peso, altura)
print(f"Seu IMC é {imc:.2f}")
