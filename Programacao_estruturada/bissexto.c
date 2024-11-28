#include <stdio.h>

int bissexto(int ano);

int main () {
    int ano =0;
    printf("Digite o valor do ano : ");
    scanf("%d", &ano);
    if (bissexto(ano)){
        printf("%d e ano bissexto \n", ano);
    }
    else
    {
        printf("%d nao e ano bissexto \n", ano);
    }
    return 0;
}

int bissexto(int ano){
    if (((ano%400 ==0)) || ((ano%4 ==0) & (ano%100 != 0))) {
        return 1;
    }
    return 0;
}