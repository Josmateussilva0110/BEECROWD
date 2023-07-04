#include <stdio.h> 
int main()
{
	int n, c;
	float x, y, t;
	scanf("%d",&n);
	for (c = 0; c < n; c++)
	{
		scanf("%f %f",&x, &y);
		if (y == 0)
		{
			printf("divisao impossivel\n");
		}
		else
		{
			t = (int) x / y;	
			printf("%.1f\n",t);
		}
	}
}