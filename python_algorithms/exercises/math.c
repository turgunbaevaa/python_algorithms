#include <stdio.h>

int main()
{
    const double PI = 3.14;
    double radius;
    double circumfernce;
    double area;

    printf("Enter the radius of the curcle: ");
    scanf("%lf", &radius);

    circumfernce = 2 * PI * radius;
    area = PI * radius * radius;

    printf("\ncircumference is: %.2lf", circumfernce);
    printf("\narea is: %.2lf", area);


    return 1;
}

