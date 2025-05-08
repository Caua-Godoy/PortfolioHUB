a = {}
gols = []
a['nome'] = input('Digite o seu nome: ')
x = int(input('Quantas partidas ele jogou?: '))

if x == 0:
    pass
else:
    for gol in range(1, x+1):
        gols.append(int(input(f'Quantos gols na partida {gol}: ')))
    print('='*30)
    a['gols'] = gols.copy()
    a['total'] = sum(gols)
    a['partidas'] = x
    print(a)
    print('='*30)
    for c , v in a.items():
        print(f'{c} = {v}')
    print('='*30)
    print(f'O jogador {a['nome']} jogou {x} partidas')
    for gol in range(x):
        print(f'-> Na partida {gol+1}, fez {a['gols'][gol]} gols')
print(f'foi um total de {a["total"]}')
        