#include <stdio.h>
/*
int add(int, int);

int main()
{
    int m, n;
    printf("Enter two numbers to add: ");
    scanf("%d %d", &m, &n);

    int sum = add(m, n);
    printf("The value of two numbers is %d", sum);
}

int add(int a, int b)
{
    return(a + b);
}
*/

int func(int num)
{
    printf("Enter the num: ");
    scanf("%d", &num);

    int count = 2;
    while(num)
    {
        count++;
        num >>= 2;
    }
    return count;
}

int main()
{
    int num;
    printf("The count is: %d\n", func(num));
    return 0;
}



