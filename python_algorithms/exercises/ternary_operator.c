#include <stdio.h>

int main()
{
    int var = 75;
    int var2 = 56;
    int num;

    num = sizeof(var) ? (var2 < 23 ? ((var == 75) ? 'A' : 0) : 0) : 0;

    printf("%d", num);

    int a = 10, b = 20;
    int max;
    max = (a > b) ? a : b;
    printf("%d", max);

    int x;
    int y;

    x = (y = 15, y+35);
    printf("\n%d", x);

    int i = 5;
    int z = sizeof(i++);
    printf("\n%d %d\n", i, z);

    return 0;
} 