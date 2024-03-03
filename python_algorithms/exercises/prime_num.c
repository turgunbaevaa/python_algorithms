#include <stdio.h>

int main() {
  int num, i, flag = 0;

  // Read the number to be checked
  printf("Enter a positive integer: ");
  scanf("%d", &num);

// Check if the number is divisible by any number less than itself
  for (i = 2; i <= num / 2; ++i) {
    if (num % i == 0) {
      flag = 1;
      break;
    }
  }

  // If flag is 0, the number is prime
  if (flag == 0)
    printf("%d is a prime number\n", num);
  else
    printf("%d is not a prime number\n", num);

  return 0;
}