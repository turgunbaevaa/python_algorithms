#include <stdio.h>

int main()
{
    float fahr, celsius;
    int lower, upper, step;
    lower = 0; /* нижняя граница таблицы температур */
    upper = 300; /* верхняя граница */
    step = 20; /* шаг */
    fahr = lower; //int привращается в значение float для проверки

    printf("Fahrenheit to Celsius: \n");

    while (fahr <= upper) {
    celsius = (5.0/9.0) * (fahr-32.0); //9.0/5.0 + 32
    printf ("%3.0f\t%6.1f\n", fahr, celsius);
    fahr = fahr + step;
    }

    printf("Fahrenheit to Celsius with for loop: \n");

    for (fahr = 300; fahr >= 0; fahr = fahr - 20) {
        celsius = (5.0/9.0) * (fahr - 32.0);
        printf("%3.0f\t%6.1f\n", fahr, celsius);
    }

    step = 5;
    upper = 150;
    celsius = lower;
    printf("Celsius to fahrenheit: \n");
    while(celsius <= upper){
        fahr = 9.0/5.0 * celsius + 32;
        printf("%6.0f\t%3.0f\n", celsius, fahr);
        celsius = celsius + step;
    }

    printf("\nCelsius to fahrenheit using for loop: \n");
    for(celsius = 0; celsius<=150; celsius = celsius+5)
    {
        fahr = 9.0/5.0 * celsius + 32;
        printf("%6.0f\t%3.0f\n", celsius, fahr);
    }

    return 0;
}