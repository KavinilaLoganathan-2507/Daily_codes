/* Get a number from the user and subtract 5 from that number
   if the number's ten's position digit is odd.
   Do not use "if".

   Input: 685    Output: 685
   Input: 89172  Output: 89167
*/

#include <stdio.h>

int main() {
    int num;

    printf("Enter the number: ");
    scanf("%d", &num);

    int tensPosition = (num / 10) % 10;

    int result = num - 5 * (tensPosition & 1);

    printf("Output: %d\n", result);

    return 0;
}
