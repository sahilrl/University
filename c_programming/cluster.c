#include <stdio.h>
#include <stdlib.h>
//global variable defined
int n;
//taking and validating user input
int userinput() {
    int check;
    int cha;
    int charr;
    printf("Enter number of elements to put in array: ");
    check = scanf("%d", &n);
    charr = scanf("%c", &cha);
    while ((check != 1) || (n < 0))  {
        printf("Your input is incorrect\n");
        printf("Please enter an postive integer: ");
        check = scanf("%d", &n);
        charr = scanf("%c", &cha);
    };
    return (n);
};


int main() {
    //taking user input for array size
    n = userinput();

    //initializing array
    int* arr = (int*) malloc(sizeof(int)*n);

    //putting elements in array
    for (int i=0; i<n; i++) {
        printf("Enter element %d: ", i+1);
        scanf("%d", &arr[i]);
    }
    //printing original array
    printf("[");
    for (int i=0; i<n; i++) {
        printf("%d, ", arr[i]);
    }
    printf("]\n");
    //limiter
    int limiter = 7;
    //counters
    int index = 0;
    int addin = 1;
    int i=0;
    int temp=0;
    //checking condition
    while (i<n) {
        temp = temp + arr[i];
        if (temp < limiter) {
            arr[index++] = addin;
            i = i+1;
        }
        else{
            if (arr[i] >= limiter) {
                i = i+1;
            }
            else {
                temp = 0;
                addin = addin + 1;
            }

        }
    }
     //printing modified array
    printf("[");
    for (int i=0; i<n; i++) {
        printf("%d, ", arr[i]);
    }
    printf("]");


    return 0;
}
