#include <stdio.h>

int main()
{
    int value, i;
    scanf("%d",&value);
    for(i = 0; i <= value; i++)
    {
        if(i % 2 != 0)
            printf("%d\n",i);
    }
}