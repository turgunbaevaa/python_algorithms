#include <stdio.h>
#define N 7

int main()
{
    int A[N] = {0};

    for(int i=0; i<N; ++i)
    A[i] = i%2; //output is 0 1 0 1 0 1 0                    
     
    //A[N - i - 1] = i; A[i] = N - i - 1; --> output: 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

    for(int i=0; i<N; ++i)
        printf(" %d", A[i]);

    return 0;
}

