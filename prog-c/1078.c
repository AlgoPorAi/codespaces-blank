/*
Problema 1078 BeeCrowd
2026.10.06
Lorenzo Waselik
*/
#include <stdio.h>

int main() {
    int n, i;

    scanf("%d", &n);

    for (i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", i, n, i * n);
    }

    return 0;
}