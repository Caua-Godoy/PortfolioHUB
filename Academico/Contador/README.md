
# 📊 Contador Personalizado em Python

Este projeto implementa um contador personalizável em Python que permite ao usuário definir o valor inicial, final e o passo da contagem. O programa também inclui algumas contagens padrão e animações simples com atrasos para visualização mais dinâmica.

## 🚀 Funcionalidades

- Contagem crescente e decrescente com passo positivo ou negativo.
- Atraso entre os números para simular uma "animação".
- Entradas personalizadas do usuário.
- Tratamento para contagens inválidas (passo negativo com contagem crescente, por exemplo).

## 🛠️ Como Funciona

A função principal do programa é:

```python
def contador(a, b, c):
```

Ela imprime uma sequência de números de `a` até `b`, com passo `c`, respeitando os seguintes critérios:

- Se `c < 0` e `a > b`: contagem decrescente.
- Se `a > b`: também contagem decrescente com passo negativo.
- Se `a < b` e `c >= 0`: contagem crescente.

## 📋 Exemplo de Uso

Ao executar o programa, ele fará:

1. Uma contagem de 1 até 10 de 1 em 1.
2. Uma contagem de 10 até 0 de 2 em 2.
3. Uma contagem personalizada com valores inseridos pelo usuário.

```bash
Digite o valor inicial: 5
Digite o valor final: 20
Digite o passo: 3
```

Saída esperada:
```
Contagem de 5 até 20 em 3:
5
8
11
14
17
20
FIM
```

## 📦 Requisitos

- Python 3.x

Não são necessárias bibliotecas externas. Apenas a biblioteca padrão `time` é usada.

## 🧠 Inspiração

Este tipo de exercício é comum em estudos de programação para aprender sobre loops, condições e entrada de dados do usuário em Python.
