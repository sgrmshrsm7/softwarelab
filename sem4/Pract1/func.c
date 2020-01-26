#include  "func.h"

int power(int a, int b)
{
	int p=1, i;
	for(i = 0 ; i < b ; i++)
	p = p * a;
	return p;
}

