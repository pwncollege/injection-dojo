#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int win()
{
	puts("You win!");
	exit(0);
}

int main()
{
	char name[16];
	puts("What is your name?");
	scanf("%s", name);

	puts("You can't win!");
}
