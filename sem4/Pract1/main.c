#include <stdio.h>
#include "func.h"

int main()
{
	int a, b;
	printf("Enter first number : ");
	scanf("%d", &a);
	printf("Enter second number : ");
	scanf("%d", &b);
	int s = power(a, b);
	printf("%d^%d = %d\n", a, b, s);
}

