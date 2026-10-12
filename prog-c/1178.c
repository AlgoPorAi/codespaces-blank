/*
Disciplina  : 2026-PCAP
Problema    : BeeCrowd 1178 - Array Fill III
Autor       : Lorenzo Waselik
LIAC        : 
*/
#include <stdio.h>

int main() {
    double n[100];
    int i;

    if (scanf("%lf", &n[0]) != 1);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2.0;
    }

    for (i = 0 ; i < 100; i++) {
        printf("N[%d] = %.4f\n", i, n[i]);
    }

    return 0;
}