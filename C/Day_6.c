//Relational operator 
#include <stdio.h>

int main() {
    int num_1,num_2;
    printf("Enter first number:");
    scanf("%d", & num_1);
    printf("Enter second number:");
    scanf("%d", & num_2);
    printf("AND %d \n", num_1 && num_2);
    printf("OR %d \n", num_1 || num_2);
    printf("NOT %d \n", ~num_2);

    return 0;
}
