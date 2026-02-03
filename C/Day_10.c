//Getting two digit number and printing the ones digit 
#include <stdio.h>

int main() {
    int num, result;
    printf("Enter two digit number:");
    scanf("%d", &num);
result = num % 10 ;
printf("the result %d \n",result);
    return 0;
}
