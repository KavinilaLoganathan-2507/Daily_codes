// Getting three digit number and printing 10's digit
#include <stdio.h>

int main() {
    int num , result;
    printf("Enter a three digit number:");
    scanf("%d" , &num);
    result = num %100;
    printf("The result is : %d \n", result / 10);
 

    return 0;
}
