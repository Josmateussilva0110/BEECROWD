#include <stdio.h>
#include <string.h>
int main()
{
	int q, i, pa, t, tam, j;
	char s[1001];
	scanf("%d",&q);
	for(i = 0; i < q; i++)
	{
		scanf("%s",&s);
		pa = 0;
		t = 0;
		tam = strlen(s);
		for(j = 0; j < tam; j++)
		{
			if(s[j] == '<')
				pa += 1;
			if(s[j] == '>' && pa > 0)
			{
				pa -= 1;
				t += 1;
			}
		}
		printf("%d\n",t);
	}
}