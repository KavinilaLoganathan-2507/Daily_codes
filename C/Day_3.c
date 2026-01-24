//Input users from and printing
#include <stdio.h>

int main() {
    int num;
    char name[10];

    printf("Enter a number: ");
    scanf("%d", &num);
    printf("The number is: %d\n", num);

    printf("Enter a name: ");
    scanf("%s", name);
    printf("The name is: %s\n", name);

    return 0;
}
