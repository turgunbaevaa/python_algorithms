#include <stdio.h>
#define N 16

int main()
{
    int A[N] = {0};

    for(int i = 0; i < N/2; ++i)
    {
        A[2*i] = i;     
        A[2*i+1] = N/2 + i;             
    } 

    for(int i = 0; i < N; ++i)
        printf(" %d", A[i]);

    return 0;
}

