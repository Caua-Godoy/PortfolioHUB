import time
def contador(a , b , c):
    print(f'Contagem de {a} até {b} de {+c} em {+c}:')
    if c < 0 and a > b:
        for n in range(a, b-1, c):
            print(n)
            time.sleep(0.2)
        print('FIM')
    elif a > b:
        for n in range(a, b-1, -c):
            print(n)
            time.sleep(0.2)
        print('FIM')

    elif c >= 0 and a < b:
        for num in range(a, b+1, c):
            print(num)
            time.sleep(0.2)
        print('FIM')
def lin():
    print('-'*30)

lin()
for num in range(1, 11, 1):
    print(num)
    time.sleep(0.2)
lin()
for num in range(10,-1, -2):
    print(num)
    time.sleep(0.2)
lin()
x = int(input('Inicio: '))
y = int(input('Fim: '))
z = int(input('Passo: ')) 


contador(x, y, z)