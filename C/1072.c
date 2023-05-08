#include <stdio.h>
int main()
{
	int x, n, c, cf = 0,cd = 0;
	scanf("%d",&n);
	for(c = 0; c < n; c++)
	{
		scanf("%d",&x);
		if (x >= 10 && x <= 20)
			cf++;
		if (x < 10 || x > 20)
			cd++;
	}
	printf("%d in\n",cf);
	printf("%d out\n",cd);
}
