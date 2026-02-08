// Getting a three digit number anad printing their sum of digits
#include <stdio.h>

int main() {
    int num, result_1,result_2,result_3,result;
    printf("Enter  three digit number:");
    scanf("%d",&num);
    result_1 = num %100;
    result_2 = num /100;
    result_3 = num %10;
    result = result_1/10;
    printf("The final result is : %d \n",result_2+result_3+result);
    return 0;
}
