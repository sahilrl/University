#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    // Creating the array
    printf("Enter the size of the Array: ");
    scanf("%d", &n);

    //int arr[max_size]
    int* arr = (int*) malloc(sizeof(int) * n);

    //taking input from the user
    for(int i=0; i<n; i++)
    {
        printf("Enter the %d of Element:", i+1);
        scanf("%d", &arr[i]);
    }
    //printing the array
    printf("[");
    for(int i = 0; i < n-1; i++)
    {
        printf("%d, ",arr[i]);
    }
    printf("%d]", arr[n-1]);

    //arranging new arr

    if (n%2 != 0)
    {
        for(int i=0; i<n/2; i++)
        {
            arr[i] = arr[i] + arr[n-i-1];
        }
        arr[n/2] = arr[n/2];

        //printing arranged array, when n is odd
        printf("[");
        for (int i=0; i<=n/2; i++ )
        {
            printf("%d,",arr[i]);
        }
        printf("]");

    }
    else {
         for(int i=0; i<=n/2; i++)
        {
            arr[i] = arr[i] + arr[n-i-1];
        }
         //printing new array when n is even
        printf("[");
        for (int i=0; i<n/2; i++)
        {
            printf("%d,",arr[i]);
        }
        printf("]");
    }

    free(arr);
    return 0;
}


