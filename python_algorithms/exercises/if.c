#include <stdio.h>

int main()
{
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);

    if(age>=18)
    {
        printf("You are adult!");
    }
    else (age<=18);
    {
        printf("Go to school!");
    }


    return 0;
}

