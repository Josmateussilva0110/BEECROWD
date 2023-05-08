#include <stdio.h>
int main()
{
	int c, n, cp = 0,ci = 0,cpo = 0,cn = 0;
	for (c = 0; c < 5; c++)
	{
		scanf("%d",&n);
		if (n % 2 == 0)
		{
			cp += 1;
		}
		if (n % 2 == 1)
		{
			ci += 1;
		}
		if (n > 0)
		{
			cpo += 1;
		}
		if (n < 0)
		{
			cn += 1;
		}
	}
	printf("%d valor(es) par(es)\n",cp);
	printf("%d valor(es) impar(es)\n",ci);
	printf("%d valor(es) positivo(s)\n",cpo);
	printf("%d valor(es) negativo(s)\n",cn);
}