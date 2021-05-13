#include<stdio.h>
#include <stdlib.h>

int inputvalidation() {
    int n;
    int check;
    int charr;
    char cha;
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


int* mat(int* r, int* c, int* arr_address){
    //local variables
    int row;
    int col;

    //user input for row and columns
    printf("Please enter row size: \n");
    row = inputvalidation();
    printf("Please enter column size: \n");
    col = inputvalidation();
    int arr[row][col];

    //int arr[max_size]
    //why I don't need malloc to define two dimensional array and I need for one dimensional array?
    //int* arr = (int*) malloc(sizeof(int) * row * col);

    /*Counter variables for the loop*/
    int i, j;
    for(i=0; i<row; i++) {
      for(j=0;j<col;j++) {
         printf("Enter value for arr[%d][%d]:", i, j);
         scanf("%d", &arr[i][j]);
      }
    }
    //Displaying array elements
    printf("Two Dimensional array elements:\n");
    for(i=0; i<row; i++) {
      for(j=0;j<col;j++) {
         printf("%d ", arr[i][j]);
         if(j==col-1){
            printf("\n");
         }
      }
    }
    //storing pointer to return
    *r = row;
    *c = col;
    *arr_address =*arr;
};

int main() {
    int row, col, arr;
    mat(&row, &col, &arr);
    printf("arr 1st: %d \n", arr);
    printf("col: %d \n", col);
    printf("row: %d", row);

    return 0;
};
