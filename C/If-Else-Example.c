# include <stdio.h>
int main()
{
    int outside, weather;
    
    printf("Enter if outside (1-True ; 0-False): ");
    scanf("%d", &outside);
    
    printf("Enter if raining (1-True ; 0-False): ");
    scanf("%d", &weather);
    
    if (outside && weather)
        printf("\nPlease use an umbrella.");
        
    else
        printf("\nDress normally.");
    
    return 0;
}
