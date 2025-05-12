def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

c = float(input("Digite a temperatura em Celsius: "))
f = celsius_para_fahrenheit(c)
print(f"{c}°C equivalem a {f}°F")
