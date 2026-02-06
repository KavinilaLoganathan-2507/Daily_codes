//Getting three digit number from user annd printing the 100's digit
#include <stdio.h>

int main() {
    int num;
    printf("Enter a three digit number:");
    scanf("%d", &num);
    printf("The result is: %d \n", num / 100);

    return 0;
}
