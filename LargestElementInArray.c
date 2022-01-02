#include<stdio.h>

int returnMax(int array[], int n)
{
    int i, max = 0;
    for (i = 0; i < n; i++)
    {
        if(array[i] > max)
        {
            max = array[i];
        }
    }
    return max;
}

int main()
{
    int array[] = {100, 20, 3, 10, 2, 300, 1, 200, 30};
    int max = returnMax(array, 9);
    printf("The maximum element in this array is %d", max);
    return 0;
}
