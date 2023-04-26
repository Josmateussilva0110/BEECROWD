#include <stdio.h>

int main()
{
    int cont = 0, i, value;
    for(i = 0; i < 5; i++)
    {
        scanf("%d",&value);
        if(value % 2 == 0)
            cont++;
    }
    printf("%d valores pares\n",cont);
}