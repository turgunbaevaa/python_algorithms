#include <stdio.h>

int main()
{
    int n, result = 0, q, rem;
    printf("Enter the number, please: ");
    scanf("%d", &n);
    q = n;

    while(q!=0)
    {
        rem = q%10;
        result = result*10 + rem;
        q = q/10;
    }

    if(result == n)
        printf("The number is polindrome");
    else
        printf("The number is not polindrome");

}