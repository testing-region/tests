/**
 * This program tests the IntegerInput class.
 *
 * @author David Saah
 * @version 1.0
 * @since 2023-02-06
 *
 */
public class TestIntegerInput {
    public static void main(String[] args) {

        // Initialise an IntegerInput input object.
        IntegerInput number = new IntegerInput();

        // Set the input parameters.
        number.setInputParameters(0, 45, "Enter a number: ");

        // Display the valid value entered.
        System.out.println(number.getValue());
    }
}
