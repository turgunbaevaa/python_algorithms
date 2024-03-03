#include <stdio.h>
#include <iso646.h>

int main()
{
    int x, y;
    scanf("%d%d", &x, &y);

    if (x>0 and y>0)
        printf("its 1st quarter");
    else if (y>0 and x<0)
        printf("its 2nd quarter");
    else if (y<0 and x<0)
        printf("its 3rd quarter");
    else if (y<0 and x>0)
        printf("its 4th quarter");
    else 
        printf("its on axis");


    for (int i = 0; i < 20; i++) {
		if (i % 2 == 0) {
			continue;
		}
		printf("%d\n", i);
	}
   
    

    return 0;
}

