/*
 * This program takes the number of classes, credits and letter grades for each course
 * and calculate the total credits and points.
 * Divides total points by total credits to calculate the GPA.
 * It displays the total credits and the gpa.
 */

import java.util.Scanner;

public class LabProgram2 {
    public static void main(String[] args) {
        Scanner getInput = new Scanner(System.in);

        System.out.print("How many classes did you take last semester?: ");
        int numClass = getInput.nextInt();

        float totalPoints = 0, totalCredits = 0;

        for (int i = 1; i <= numClass; i++) {
            float credits, points;
            String letterGrade;

            System.out.printf("How many credits was course #%s?: ", i);
            credits = getInput.nextFloat();

            System.out.print("What was your letter grade?: ");
            letterGrade = getInput.next();

            switch (letterGrade) {
                case "A":
                    points = (float) 4.0;
                    break;
                case "B+":
                    points = (float) 3.5;
                    break;
                case "B":
                    points = (float) 3.0;
                    break;
                case "C+":
                    points = (float) 2.5;
                    break;
                case "C":
                    points = (float) 2.0;
                    break;
                case "D+":
                    points = (float) 1.5;
                    break;
                case "D":
                    points = (float) 1.0;
                    break;
            
                default:
                    points = (float) 0.0;
                    break;
            }

            totalCredits += credits;
            totalPoints += points * credits;

        }

        float gpa = totalPoints / totalCredits;

        System.out.println();
        System.out.printf("You took %.2f credits\n", totalCredits);
        System.out.printf("Your semester GPA was %.2f\n", gpa);
        getInput.close();
    }
}
