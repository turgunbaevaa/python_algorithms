#include <stdio.h>
 
int main()
{
    float fahrenheit, celsius;

    printf("Enter degree in Fahrenheit: ");
    scanf("%f", &fahrenheit);

    celsius = (fahrenheit - 32) * 5 / 9;
    
    printf("Temperature in Celsius: %.2f\n", celsius);

    // (5 °C × 9/5) + 32 = 41 °F

    fahrenheit = (celsius * 9/5) + 32;

    printf("Temperature in Fahrenheit: %.2f\n", fahrenheit);



    return 0;
}