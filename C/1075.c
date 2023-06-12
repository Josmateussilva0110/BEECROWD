#include <stdio.h>
 
int main() 
{
 
    int n, c;
    scanf("%d",&n);
    for (c = 1; c <= 10000; c++)
    {
        if(c % n == 2)
        {
            printf("%d\n",c);
        }
    }
}