#include<stdio.h>

int main()
{
    char s[] = "Harrys", temp;
    int len = 0, i;
    
    while (s[len] != '\0')
    {
        len++;
    }
    printf("Length of the string is %d\n", len);
    
    for (i = 0; i < (len-1)/2; i++)
    {
        temp = s[i];
        s[i] = s[len - 1 - i];
        s[len - 1 - i] = temp;
    }
    
    printf("Reversed String: %s", s);
    
    return 0;
}
