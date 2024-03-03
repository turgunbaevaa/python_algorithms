#include <stdio.h>

int main()

{
    int n = 5;
    /*
    int num1=0, num2 = 0;

    for(int i = 0; i < 10; i++, num1++)
        for(int j = 0; j < 100; j++, num1++);   

    for(int i = 0; i < 100; i++, num2++)
        for(int j = 0; j < 10; j++, num2++);    
    
    printf("First equal to %d", num1);
    printf("\nSecond equal to %d\n", num2);

    int i = 1, j = 3;
    do
    {
        do
        {
            printf("%d", j);
            j--;
        } while (j > 0);
        i++;
        printf("%d", i);

    } while (i < 4);

    int columns;
    int rows;

    printf("\nEnter number of rows: ");
    scanf("%d", &rows);

    printf("Enter number of columns: ");
    scanf("%d", &columns);

    for(i = 1; i <= rows; i++)
    {
        for(j = 1; j <= columns; j++)
        {
            printf("%d", j);
        }
    printf("\n");
    }
    
    for(int i = 1; i <= 10; i++)
    {
        printf("%d\n", i);
    }

    for(int i = 0; i < 2; i++)
    {
        for(int j = 0; j < 2; j++)
        printf("%d", j); //0101
    }

    

    

    for(int i = 1; i <= n; i++)
    {
        for(int j = i; j <= n; j++)
        {
            printf("  ");
        }        
        for(int j = 1; j <= i; j++)
        {
            printf(" *");
        }
        
    printf("\n"); 
    } 
    Output: 
           *
         * *
       * * *
     * * * *
   * * * * *
 
    for(int i = 1; i <= n; i++)
    {
        for(int j = i; j <= n; j++)
        {
            printf(" ");
        }        
        for(int j = 1; j <= i; j++)
        {
            printf(" *");
        }
        
    printf("\n"); 
    } 
    Output: 
      *
     * *
    * * *
   * * * *
  * * * * *

*/
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= i; j++)
        { 
            printf("  ");
        }        
        for(int j = i; j <= n; j++)
        {
            printf("* ");
        }
        
    printf("\n"); 
    } 


  return 0;
}