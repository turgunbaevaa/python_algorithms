#include <stdio.h>
#include <iso646.h>
#include <stdbool.h>
int main()
{
    int number;
    scanf("%d", &number);

    bool any = false;
    bool all = true;

    while(number)
    {
        int digit = number%10;
        any = any or (digit<5);
        all = all and (digit<5);
        number/=10;

    }
    printf("any = %d\n"
            "all = %d\n", any, all);

    return 0;
}