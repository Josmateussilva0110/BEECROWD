#include <stdio.h>

int main()
{
	int n, c, maior = 0, cont = 0, t;
	for (c = 1; c <= 100; c++)
	{
		scanf("%d",&n);
		cont ++;
		if (n > maior)
		{
			maior = n;
			t = cont;
			
		}
	}
		printf("%d\n",maior);
		printf("%d\n",t);
		return 0;
}
