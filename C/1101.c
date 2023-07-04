#include <stdio.h>
int a, b, c, i, sum = 0;

int invert_ab() {
        c = a;
        a = b;
        b = c;
}

int main() {

    scanf("%d %d", &a, &b);
 
    while (a > 0 && b > 0) {   
        if (a > b) invert_ab();
        
        for (i = a; i <= b; i++) {
            printf("%d ", i);
            sum = sum + i;
        }
        
        printf("Sum=%d\n", sum);

        scanf("%d %d", &a, &b);

        sum = 0;
    }

    return 0;
}