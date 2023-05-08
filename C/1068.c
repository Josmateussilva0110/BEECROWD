#include <stdio.h>
#include <string.h>

int main()
{
	char s[1001];
	int c, t, i;
	while(scanf("%s",s) != EOF)
	{
		c = 0;
		t = strlen(s);
		for(i = 0; i < t; i++)
		{
			if(s[i] == '(')
				c += 1;
			if(s[i] == ')')
			{
				if(c > 0)
				{
					c -= 1;
				}
				else
					break;
			}
		}
		if(i == t && c == 0)
			printf("correct\n");
		else
			printf("incorrect\n");
	}
}
