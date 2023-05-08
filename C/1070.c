#include <stdio.h>

int main()
{
	int n, i = 0, t;
	scanf("%d",&n);
	t = n;
	while(i < 6)
	{
		if(t % 2 != 0)
		{
			printf("%d\n",t);
			i++;
		}
		t++;
	}
}
