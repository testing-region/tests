import java.util.Scanner;

/**
 * This class handles integer input validation based on given constraints.
 * The constraints are a maximum and a minimum value.
 *
 * @author David Saah
 * @version 1.0
 * @since 2023-01-27
 *
 */
public class IntegerInput {

    // Initialise IntegerInput attributes
    private int min;
    private int max;
    private String prompt;

    /**
     * Gets the minimum value.
     *
     * @return the minimum value an input cannot be less than
     *
     */
    public int getMin() {
        return min;
    }

    /**
     * Gets the maximum value
     *
     * @return the maximum value an input cannot exceed
     *
     */
    public int getMax() {
        return max;
    }

    /**
     * Gets the input message prompt
     *
     * @return the prompt message to display before getting user input
     *
     */
    public String getPrompt() {
        return prompt;
    }

    /**
     * Sets the input parameters for the class object.
     *
     * @param min    the minimum value an input cannot go below
     * @param max    the maximum value an input cannot exceed
     * @param prompt the message to display before receiving inpput from the user
     *
     */
    public void setInputParameters(int min, int max, String prompt) {
        this.min = min;
        this.max = max;
        this.prompt = prompt;
    }

    /**
     * Gets an integer from the user and tests if it satisfies the constraints.
     * A valid integer is between the maximum and minimum value.
     *
     * @return the valid input the user enters.
     *
     */
    public int getValue() {

        // Get input using Scanner object
        Scanner getInput = new Scanner(System.in);

        // Display prompt and get value from user
        System.out.print(getPrompt());
        int value = getInput.nextInt();

        // Keep asking the user for a number until it is within the allowed range
        while (value <= getMin() || value >= getMax()) {
            System.out.println();

            System.out.println("Error: The number you entered is outside the range.");
            System.out.printf("[!] Info: Allowed range = %d - %d\n", getMin(), getMax());

            System.out.println();

            System.out.print(getPrompt());
            value = getInput.nextInt();
        }

        // close Scanner object to prevent memory leaks
        getInput.close();
        return value;
    }
}

/*
 * How This Class Could Have Been Used In The Game of Stones
 *
 * The class could have been used to validate the number of stones a player is
 * allowed to pick.
 * The constraints would have been the stones limit for each player and the
 * prompt can be modified to display messages specific for each player.
 *
 */
