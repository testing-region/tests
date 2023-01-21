/*
 * This program accepts a list of positive number, one per line
 * and counts and displays total number of even, odd and "zero" numbers
 */

import java.util.Scanner;

public class LabProgram1 {
    public static void main(String[] args) {
        System.out.println("Enter a list of positive numbers, one per line.");
        System.out.println("Use a negative number to indicate the end of input.");
        System.out.println();

        int even = 0, odd = 0, zero = 0;
        Scanner getInput = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = getInput.nextInt();

        while (num >= 0) {
            if (num == 0) {
                zero += 1;
            } else if (num % 2 == 0) {
                even += 1;
            } else {
                odd += 1;
            }

            System.out.print("Enter a number: ");
            num = getInput.nextInt();
        }

        System.out.println();
        System.out.println("Thank you!");
        System.out.printf("You entered %d even numbers, %d odd numbers and %d zeros\n", even, odd, zero);
        getInput.close();
    }
}
