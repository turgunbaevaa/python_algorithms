#include <stdio.h>

//switch = A more efficient alternative to using many else if statements
//         allows a value to be tested for equality against many cases

int main()
{
    char grade;
    printf("Hello! Enter your grade: ");
    scanf("%c", &grade);

    switch (grade){
        case 'A':
            printf("It's perfect!\n");
            break;
        case 'B':
            printf("It's good!");
            break;
        case 'C':
            printf("It's normal, not bad");
            break;
        case 'D':
            printf("You failed:(");
            break;
        default:
            printf("Enter only valid gardes!");
    }

    return 0;
}

