#include <stdio.h>
 
int main() {
    float n, soma = 0, m;
    int cont = 0, c;
    for(c = 0; c < 6; c++)
    {
        scanf("%f",&n);
        if (n > 0)
        {
           cont += 1; 
           soma += n;
           m = soma / cont;
        }
    }
    printf("%d valores positivos\n",cont);
    printf("%.1f\n",m);
 
    return 0;
}