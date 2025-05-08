numerico = []
pares_temp = []
impares_temp = []

for num in range(7):
    numero= float(input('Digite um numero: '))
    if numero % 2 == 0:
        pares_temp.append(numero)

    else:
        impares_temp.append(numero)


numerico.append(pares_temp[:])
numerico.append(impares_temp[:])
pares_temp.clear()
impares_temp.clear()


print(f'A ordem crescente dos numeros pares é: {sorted(numerico[0])}')
print(f'A ordem crescente dos numeros impares é: {sorted(numerico[1])} ')