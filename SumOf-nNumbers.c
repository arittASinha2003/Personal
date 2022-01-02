#include<stdio.h>

int main()
{
    int n, i, sum = 0;
    
    printf("Enter the last number as far as the sum you want: ");
    scanf("%d", &n);
    
    //Runs in Linear Time
    
    /*for (i = 1; i <= n; i++)
    {
        sum += i;
    }*/
    
    //Runs in Constant Time
    
    sum = (n * n + n) / 2;
    
    printf("Sum of 1st %d natural numbers: %d\n", n, sum);
    
    return 0;
}
