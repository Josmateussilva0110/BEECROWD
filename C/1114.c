#include <stdio.h>
int main()
{
	int n;
	while (1)
	{
		scanf("%d",&n);
		if (n != 2002)
		{
			printf("Senha Invalida\n");
		}
		if (n == 2002)
		{
			printf("Acesso Permitido\n");
			break;
		}
	}
}
