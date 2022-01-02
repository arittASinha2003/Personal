#include<stdio.h>

int main()
{
    int num, i;
    
    printf("Enter the number whose multiplication table is to be printed: ");
    scanf("%d", &num);
    
    printf("Multiplication Table of %d:\n", num);
    for (i = 1; i<=10; i++)
    {
        printf("%d X %d = %d\n", num, i, i*num);
    }
    return 0;
}
