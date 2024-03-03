#include <stdio.h>

int main()
{
    int i, j, n=1, rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    for(i = 1; i <= rows; i++)
    {
        for(j = 1; j <= i; j++)
        {
            printf("%d ", n);
            n++;
        }
        printf("\n");
    }

    return 0;

}