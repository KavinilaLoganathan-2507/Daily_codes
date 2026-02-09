// getting two digit and printing their reverse
#include <stdio.h>

int main() {
    int num,result,result_1,result_2;
    printf("Enter a two digit number:");
    scanf("%d", &num );
    result = num % 10;
    result_1 = num / 10;
    result_2 = result * 10 + result_1;
    printf("The final result is %d \n",result_2);
    return 0;
}
