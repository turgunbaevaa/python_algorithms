#include <stdio.h>

int main()
{
    /*
    int x = 10;
    x%=3;
    printf("%d", x);
    */
    char name [25];
    int age;

    printf("How old are you?\n");
    scanf("%d", &age);

    printf("\nWhat is your name?\n");
    scanf("%s", &name);

    printf("\nYou are %d years old", age);
    printf("\nYour name is %s", name);

    return 0;
}
