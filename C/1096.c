#include <stdio.h>

int main()
{
	int i =1, j= 7, r = 0, t = 0;
	while(t != 3 && r != 3)
	{
		printf("I=%d J=%d\n",i,j);
		j--;
		t++;
		if(i == 9)
			r++;
		if(t == 3)
		{
			i+= 2;
			j = 7;
			t = 0;
		}
	}
}
