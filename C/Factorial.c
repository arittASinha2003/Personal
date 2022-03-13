#include<stdio.h>

int factorial(int n)
{
    int i, val = 1;
    for (i = n; i > 1; i--)
    {
        val *= i;
    }
    return val;
}

int factorialRecursive(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }
    else
    {
        return n * factorialRecursive(n-1);
    }
}

int main()
{
    int n, fact;
    
    printf("Enter the number: ");
    scanf("%d", &n);
    
    //fact = factorial(n);
    fact = factorialRecursive(n);
    
    printf("Factorial of %d : %d", n, fact);
    
    return 0;
}
