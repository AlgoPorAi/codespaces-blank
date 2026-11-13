/*
Disciplina  : 2026-PCAP
Problema    : BeeCrowd 1174 - Selecao em vetor I
Autor       : Lorenzo Waselik
LIAC        : Le cem valores, 1 por linha
*/
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    vector<double> a;
    double x;
    int i, qtd;

    for (i = 0; i < 100; i++) {
        cin >> x;
        a.push_back(x);
    }

    qtd = a.size();
    cout << fixed << setprecision(1);
    for (i = 0; i < qtd; i++) {
        if (a[i] <= 10) {
            cout << "A[" << i << "] = " << a[i] << endl;
        }
    }

    return 0;
}