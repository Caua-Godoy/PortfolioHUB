
# ⚽ Registro de Gols de um Jogador em Python

Este projeto é um script simples em Python que permite registrar a performance de um jogador de futebol, informando quantos gols ele fez em cada partida jogada.

## 🚀 Funcionalidades

- Registro do nome do jogador.
- Entrada do número de partidas jogadas.
- Registro da quantidade de gols em cada partida.
- Cálculo e exibição do total de gols marcados.
- Apresentação detalhada de desempenho por partida.

## 🛠️ Como Funciona

O programa solicita ao usuário:

1. O nome do jogador.
2. O número de partidas jogadas.
3. A quantidade de gols feitos em cada partida.

Com esses dados, o programa:
- Armazena as informações em um dicionário (`a`).
- Utiliza uma lista (`gols`) para registrar os gols por partida.
- Exibe as informações no console em um formato organizado.

## 📋 Exemplo de Uso

```bash
Digite o seu nome: João
Quantas partidas ele jogou?: 3
Quantos gols na partida 1: 1
Quantos gols na partida 2: 0
Quantos gols na partida 3: 2
```

Saída esperada:
```
==============================
{'nome': 'João', 'gols': [1, 0, 2], 'total': 3, 'partidas': 3}
==============================
nome = João
gols = [1, 0, 2]
total = 3
partidas = 3
==============================
O jogador João jogou 3 partidas
-> Na partida 1, fez 1 gols
-> Na partida 2, fez 0 gols
-> Na partida 3, fez 2 gols
foi um total de 3
```

## 📦 Requisitos

- Python 3.x

Não são necessárias bibliotecas externas.

## 🧠 Inspiração

Este projeto é um exemplo prático para iniciantes em Python sobre o uso de dicionários, listas e loops, aplicados em um cenário esportivo.
