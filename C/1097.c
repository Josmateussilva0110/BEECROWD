#include <stdio.h>

int main()
{
	int i = 1, j = 7, i1;
	while(i <= 9)
	{
		for(i1 = 0; i1 < 3; i1++)
		{
			printf("I=%d J=%d\n",i,(j-i1));
		}
		i+= 2;
		j+= 2;
	}
}
