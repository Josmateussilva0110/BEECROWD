#include <stdio.h>

int main()
{
	int c, n;
	float n1, n2, n3, t;
	scanf("%d",&n);
	for(c = 0; c < n; c++)
	{
		scanf("%f %f %f",&n1, &n2, &n3);
		t = (n1 * 2 + n2 * 3 + n3 * 5) / 10;
		printf("%.1f\n",t);
	}
}