
# 🔢 Módulo de Operações Matemáticas com Python

Este projeto demonstra a utilização de um módulo personalizado em Python para realizar operações matemáticas simples, como cálculo de fatorial e do dobro de um número.

## 🚀 Funcionalidades

- Cálculo do fatorial de um número inteiro.
- Cálculo do dobro de um número inteiro.
- Organização do código em módulos para melhor reutilização.

## 🛠️ Como Funciona

O script principal (`teste5.py`) importa funções do módulo `uteis.numeros.teste1` e executa as seguintes etapas:

1. Solicita um número inteiro ao usuário.
2. Calcula o fatorial do número.
3. Calcula o dobro do número.
4. Exibe os resultados no console.

## 📁 Estrutura Esperada do Projeto

```
seu_projeto/
├── teste5.py
└── uteis/
    └── numeros/
        └── teste1.py
```

O módulo `teste1.py` deve conter, pelo menos, as seguintes funções:
- `fatorial(n)`
- `dobro(n)`

## 📋 Exemplo de Uso

```bash
Digite um valor: 5
```

Saída esperada:
```
o fatorial de 5 é 120
o dobro de 5 é 10
```

## 📦 Requisitos

- Python 3.x
- Módulo `uteis.numeros.teste1` com as funções `fatorial()` e `dobro()` implementadas.

## 🧠 Inspiração

Este projeto reforça conceitos de modularização em Python, mostrando como separar lógicas em arquivos reutilizáveis.
