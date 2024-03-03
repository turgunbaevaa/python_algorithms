#include <stdio.h>
#include <math.h>


void print_number_factors(int x)
{
    printf("Number factors: ");
    int divisor = 2;
    while (x != 1)
    {
        while (x%divisor == 0)
        {
            printf("%d", divisor);
            x/=divisor;
        }
        divisor += 1;
    }
    printf("\n");
}