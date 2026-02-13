// Get a three-digit number from user and print the reverse of the number

#include <stdio.h>
int main(){
    int num, digit, digit_1, digit_2, digit_3, reverse;
    printf("Enter a 3-digit number: ");
    scanf("%d", &num);
    digit_1 = num/100;
    digit = num%100;
    digit_2 = digit/10;
    digit_3 = num%10;
    reverse = (digit_3*100)+(digit_2*10)+digit_1;
    printf("Reversed number: %d", reverse);
    return 0;
}
