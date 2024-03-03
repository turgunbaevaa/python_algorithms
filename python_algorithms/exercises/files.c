#include <stdio.h>

int main()
{
    char line[255];
    FILE *file = fopen("main.txt", "r");

    fgets(line, 255, file);
    printf("%s", line);
    fgets(line, 255, file);
    printf("%s", line);
    fgets(line, 255, file);
    printf("%s", line);

    fclose(file);

    return 0;
}