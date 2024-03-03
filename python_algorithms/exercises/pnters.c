#include <stdio.h>

int main()
{
    int num = 0;
    int * pnum = &num;
    * pnum = 10;
    printf("%d", * pnum);



    return 0;
}