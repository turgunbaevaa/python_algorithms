#include <stdio.h>
#include <iso646.h>
#include <stdbool.h>
/*
int main(int argc, char* argv[])
{
    int x, i;
    int m = -1999, m_i;
    scanf("%d", &x);

    while(x != 0)
    {
        if (x%2==0)
            if(x>m)
            {
                m = x;
                m_i = i;
            }
        i += 1;
        scanf("%d", &x);

    }

    printf("maximum = %d\n",
    "maximum position = %d\n", m, m_i);

    return 0;
}
*/

#include <stdio.h>

int max(int a[], int n) {
    if (n == 1) {
        return a[0];
    }
    int m = max(a, n-1);
    return (a[n-1] > m) ? a[n-1] : m;
}

int main() {
    int a[] = {1, 3, 5, 2, 8, 4};
    int n = sizeof(a) / sizeof(a[0]);
    printf("Maximum value: %d", max(a, n));
    return 0;
}