# Exercício de Lógica de Programação - Comparação e Operações em Python

Este repositório contém uma solução para um exercício prático de lógica de programação e algoritmos, focado em estruturas condicionais e operações aritméticas simples de uma série de exercícios passados pelo professor.

## 📝 O Problema
O objetivo do algoritmo é receber dois números inteiros positivos do usuário e realizar as seguintes operações:

1- Verificar se o segundo número é ímpar.
2- Caso seja, realizar a subtraçao do primeiro número do segundo.
3- Se o segundo número for ímpar, realizar a divisão do segundo pelo primeiro número.

## 🛠️ Lógica Aplicada (Pseudocódigo)

Abaixo está a representação da lógica utilizada:

INÍCIO

    // Entrada de dados inicial
    ESCREVA "Digite um número: "
    LEIA x
    ESCREVA "Digite o segundo número: "
    LEIA y

    // Validação para garantir números positivos
    ENQUANTO (x < 0) OU (y < 0) FAÇA
        ESCREVA "Erro: os números devem ser inteiros e positivos"
        ESCREVA "Digite um número: "
        LEIA x
        ESCREVA "Digite o segundo número: "
        LEIA y
    FIM_ENQUANTO


    // Verificação de paridade e cálculo
    SE (y MOD 2 = 0) ENTÃO
        resultado <- y - x
    SENÃO
        resultado <- y / x
    FIM_SE

    // Saída final
    ESCREVA "O resultado é: ", resultado

FIM

