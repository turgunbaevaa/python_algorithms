#include <stdio.h>

int main()
{
    int x;
    scanf("%d", &x);

    int p = 1;
    while(x)
    {
        int digit = x%10;
        p *= digit;
        x/=10;

    }
    printf("Result = %d", p);

    return 0;
}