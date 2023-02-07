/**
 * This program tests the Person class.
 *
 * @author David Saah
 * @version 1.0
 * @since 2023-02-06
 *
 */
public class TestPerson {
    public static void main(String[] args) {

        // Create a Person object and define parameters using setPerson method
        Person person1 = new Person();
        person1.setPerson(
                "David Saah",
                (byte) 20,
                "Male");

        // Display the attributes of person1 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n",
                person1.getName(), person1.getAge(), person1.getGender());

        System.out.println();

        // Create a Person object with an invalid age
        Person person2 = new Person();
        person2.setPerson(
                "Dr. John Edem",
                (byte) -18,
                "Male");

        // Display the attributes of person2 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n",
                person2.getName(), person2.getAge(), person2.getGender());

        /*
         * NOTE: To see the effect of person3 object, comment out the person2 object's
         * initialisation and operations.
         * Reason: The program exits if an invalid age is entered.
         */

        System.out.println();

        // Create a Person object with an invalid gender
        Person person3 = new Person();
        person3.setPerson(
                "John Doe",
                (byte) 67,
                "Deceased");

        // Display the attributes of person3 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n",
                person3.getName(), person3.getAge(), person3.getGender());
    }
}
