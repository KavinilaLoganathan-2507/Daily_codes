//Arithmetic operation
#include <stdio.h>
int main()
{
  int num_1,num_2;
  printf("Enter first number:",num_1);
  scanf("%d", &num_1);
  printf("Enter second number: ",num_2);
  scanf("%d", &num_2);
  printf("addition %d\n",num_1 + num_2);
  printf("difference  %d\n",num_1 - num_2);
  printf("product %d\n",num_1 * num_2);
  printf("division %d\n",num_1 / num_2);
  printf("reminder %d\n",num_1 % num_2);
  return 0;
}
