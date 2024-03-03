#include <stdio.h>

int main()
{
    int i = 1;
    while(i <= 3)
    {
        printf("meow ");
        i = i+1;
    }

    int buf;
    printf("\nHow many times your dog should buf? ");
    scanf("%d", &buf);
    for(int i = 1; i <= buf; i++)
    {
        printf("buf ");
    }





    return 0;
}