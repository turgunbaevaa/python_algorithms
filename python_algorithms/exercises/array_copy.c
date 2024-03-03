#include <stdio.h>
#include <stdlib.h>

void arrayCopy(int *source, int *dest, int size) {
    for (int i = 0; i < size; i++) {
        *(dest + i) = *(source + i);
    }
}

int main()
{
    int sourceArray[] = {1, 2, 3, 4, 5};
    int destArray[5];
    int size = 5;

    arrayCopy(sourceArray, destArray, size);

    for (int i = 0; i < size; i++) {
        printf("%d ", destArray[i]);
    }
    printf("\n");

    return 0;
}

