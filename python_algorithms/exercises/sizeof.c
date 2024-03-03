// C program to find the size of int, char,
// float and double data types

#include <stdio.h>

int main()
{
	int integerType;
	char charType;
	float floatType;
	double doubleType;

	// Calculate and Print
	// the size of integer type
	printf("\nSize of int is: %ld",
		sizeof(integerType));

	// Calculate and Print
	// the size of charType
	printf("\nSize of char is: %ld",
		sizeof(charType));

	// Calculate and Print
	// the size of floatType
	printf("\nSize of float is: %ld",
		sizeof(floatType));

	// Calculate and Print
	// the size of doubleType
	printf("\nSize of double is: %ld",
		sizeof(doubleType));

	return 0;
}
