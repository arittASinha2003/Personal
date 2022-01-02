#include<stdio.h>

int main(){
    int n, i, isPrime = 1;

    printf("Enter the number: ");
    scanf("%d", &n);

    for (i = 2; i * i < n; i++)
    {
        if (n % i == 0)
        {
            isPrime = 0;
        }
    }

    if (isPrime)
    {
        printf("%d is a prime number\n", n);
    }
    else
    {
        printf("%d is a composite number\n", n);
    }
    return 0;
}
