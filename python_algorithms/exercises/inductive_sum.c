#include <stdio.h>

int main()
{
    int x;
    scanf("%d", &x);

    int s = 0;
    while(x)
    {
        int digit = x%10;
        s+=digit;
        x/=10;

    }
    printf("Result = %d", s);

    return 0;
}