#include<stdio.h>

int reverse(int n)
{
    int rev = 0, rem;
    while (n != 0)
    {
        rem = n % 10;
        rev = rev * 10 + rem;
        n = n / 10;
    }
    return rev;
}

int main()
{
    int n, rev;
    
    printf("Enter the number: ");
    scanf("%d", &n);
    
    rev = reverse(n);
    
    printf("Reversed Number : %d", rev);
    
    return 0;
}
