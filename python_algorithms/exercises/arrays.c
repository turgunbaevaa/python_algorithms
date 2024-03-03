#include <stdio.h>
#define N 10

    void print_array(int A[])
    {
        for(int i = 0; i < N; i++)
            printf(" %3d", A[i]);
        printf("\n");
    }

int main(){

    int A[N] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90};
    int B[N] = {0};
    
    for(int i = 0; i < N; i++)
        B[i] = A[i];
    
    print_array(A);
    print_array(B);

//Reverse copy function

    for(int i = 0; i < N; i++)
        B[i]=A[N-1-i];

    print_array(B);

//Нециклический сдвиг влево
    for(int i = 0; i < N/2; i++)
    {
        int tmp = A[i];
        A[i] = A[N-1-i];
        A[N-1-i] = tmp;
    }
    print_array(A);

//Циклический сдвиг влево

    int tmp = A[0];
    for(int i = 0; i < N-1; i++)
        A[i] = A[i+1];
    A[N-1] = tmp;
    print_array(A);


    return 0;
}