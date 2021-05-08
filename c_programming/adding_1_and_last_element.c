#include <stdio.h>
#include <stdlib.h>

//globals
int n;
char cha;
//validation
int userinput() {
    int check;
    int charr;
    check = scanf("%d", &n);
    charr = scanf("%c", &cha);
    while ((check != 1) || (n < 0))  {
        printf("Your input is incorrect\n");
        printf("Enter +ve number: ");
        check = scanf("%d", &n);
        charr = scanf("%c", &cha);
    };
    return (n);
};


int main() {
    //local variables
    char cha;
    // Creating the array
    printf("Enter number of elements to put in array: ");
    n = userinput();

    //int arr[max_size]
    int* arr = (int*) malloc(sizeof(int) * n);

    //taking input from the user
    for(int i=0; i<n; i++)
    {
        printf("Enter the %d Element:", i+1);
        while (scanf("%d", &arr[i]) != 1) {
            scanf("%c", &cha);
            printf("You didn't enter +ve number. Try again...\n");
            printf("Re-enter %d Element:", i+1);
        };

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


