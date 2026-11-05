/*
Disciplina  : 2026-PCAP
Problema    : BeeCrowd 1004 - Produto Simples
Autor       : Lorenzo Waselik
LIAC        : Le dois inteiros A e B, um por linha. Imprime o produto no formato "PROD = resultado", com espacos em volta do sinal de igual
*/
#include <iostream>

int main() {
    int a, b;

    std::cin >> a >> b;
    std::cout << "PROD = " << a * b << std::endl;

    return 0;
}