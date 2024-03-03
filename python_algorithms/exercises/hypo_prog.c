#include <stdio.h>
#include <math.h>

int main()
{

    double A;
    double B;
    double C;

    printf("Enter A side: ");
    scanf("%lf", &A);

    printf("Enter B side: ");
    scanf("%lf", &B);

    C = sqrt(A*A + B*B);

    printf("Side C is equal to %.2lf", C);

    return 0;
}

