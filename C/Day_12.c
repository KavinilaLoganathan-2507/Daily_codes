//Getting three digit number from user and printing the one's digit 
#include <stdio.h>

int main() {
    int num, result;
    printf("Enter a three digit number:");
    scanf("%d", &num);
    result = num % 10;
    printf("the result is : %d \n",result);
    
    return 0;
}
