#include <stdio.h>

int main()
{
    int value;
    scanf("%d",&value);
    for(int i = 1; i <= value; i++)
    {
        if(i % 2 == 0)
            printf("%d^2 = %d\n",i, i * i);
    }
}