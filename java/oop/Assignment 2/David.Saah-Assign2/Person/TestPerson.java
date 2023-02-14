/**
 * This program tests the Person class.
 *
 * @author David Saah
 * @version 2.0
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
                "male");

        // Display the attributes of person1 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n",
                person1.getName(), person1.getAge(), person1.getGender());

        System.out.println();

        // Create a Person object to use the default values of the class constructor
        Person person2 = new Person();

        // Display the attributes of person2 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n",
                person2.getName(), person2.getAge(), person2.getGender());

        System.out.println();

        // Create a Person object and set field values using constructor
        Person person3 = new Person(
            "Ada Lovelace",
            (byte) 43,
            "female"
        );

        // Display the attributes of person3 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n",
                person3.getName(), person3.getAge(), person3.getGender());

        System.out.println();

        // Create a Person object with an invalid age
        Person person5 = new Person();
        person5.setPerson(
                "Dr. John Edem",
                (byte) -18,
                "male");

        // Display the attributes of person5 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n",
                person5.getName(), person5.getAge(), person5.getGender());

        /*
         * NOTE: To see the effect of person5 object, 
         * comment out the person2 object's initialisation and operations.
         * 
         * REASON: The program exits if an invalid age is entered.
         * 
         */

        System.out.println();

        // Create a Person object with an invalid gender
        Person person6 = new Person();
        person6.setPerson(
                "John Doe",
                (byte) 67,
                "Deceased");

        // Display the attributes of person6 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n",
                person6.getName(), person6.getAge(), person6.getGender());
    }
}
