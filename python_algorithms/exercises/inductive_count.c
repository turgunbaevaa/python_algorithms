#include <stdio.h>

int main()
{
    int x;
    scanf("%d", &x);

    int n = 0;
    while(x)
    {
        int digit = x%10;
        n+=1;
        x/=10;

    }
    printf("Result = %d", n);

    

    return 0;
}