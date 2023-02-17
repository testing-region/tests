/**
 * This program tests the Person class.
 *
 * @author David Saah
 * @version 2.0
 * @since 2023-02-06
 *
 */
public class TestPerson {

    /**
     * Checks if the person objects are equal
     * 
     * @param self  main person object
     * @param other other person object
     * 
     */
    public static void testEquals(Person self, Person other) {
        if (self.equals(other)) {
            System.out.println("The person objects are equal\n");
        } else {
            System.out.println("The person objects are not equal\n");
        }
    }

    /**
     * Checks to see if a person is younger than the other
     * 
     * @param self  main person object
     * @param other other person object
     * 
     */
    public static void testYoungerPerson(Person self, Person other) {
        if (self.isYounger(other)) {
            System.out.printf("%s is younger than %s\n\n",
                    self.getName(), other.getName());
        } else {
            System.out.printf("%s is not younger than %s\n\n",
                    self.getName(), other.getName());
        }
    }

    /**
     * Checks to see if a person is older than the other
     * 
     * @param self  main person object
     * @param other other person object
     * 
     */
    public static void testOlderPerson(Person self, Person other) {
        if (self.isOlder(other)) {
            System.out.printf("%s is older than %s\n\n",
                    self.getName(), other.getName());
        } else {
            System.out.printf("%s is not older than %s\n\n",
                    self.getName(), other.getName());
        }
    }

    /**
     * Checks whether two person objects have the same name
     * 
     * @param self  main person object
     * @param other other person object
     */
    public static void testSameName(Person self, Person other) {
        if (self.isSameName(other)) {
            System.out.println("The person objects have the same name\n");
        } else {
            System.out.println("The person objects do not have the same name\n");
        }
    }

    /**
     * Checks whether two person objects have the same age
     * 
     * @param self  main person object
     * @param other other person object
     */
    public static void testSameAge(Person self, Person other) {
        if (self.isSameAge(other)) {
            System.out.println("The person objects have the same age\n");
        } else {
            System.out.println("The person objects do not have the same age\n");
        }
    }

    /**
     * The main method runs the tests
     * 
     * @param args
     * 
     */
    public static void main(String[] args) {
        // Create a Person object and define parameters using setPerson method
        Person person1 = new Person();
        person1.setPerson("David Saah", 20, "male");

        // Display the attributes of person1 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n\n",
                person1.getName(), person1.getAge(), person1.getGender());

        // Create a Person object to use the default values of the class constructor
        Person person2 = new Person();

        // Display the attributes of person2 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n\n",
                person2.getName(), person2.getAge(), person2.getGender());

        // Create a Person object and set field values using constructor
        Person person3 = new Person("Ada Lovelace", 43, "female");

        // Display the attributes of person3 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n\n",
                person3.getName(), person3.getAge(), person3.getGender());

        // clone person3
        Person person3Clone = person3;

        /*
         * Testing the properties of objects.
         * Case 1: Objects are equal (same name and age).
         * Case 2: One person is older than the other.
         * Case 3: One person is younger than the other.
         * Case 4: Objects have the same name.
         * Case 5: Objects have the same age.
         *
         */

        // Case 1: Objects are not equal
        testEquals(person1, person3);

        // Case 1: Objects are equal
        testEquals(person3, person3Clone);

        // Case 2: First person is older
        testOlderPerson(person3, person1);

        // Case 2: First person is not older
        testOlderPerson(person1, person3);

        // Case 3: First person is younger
        testYoungerPerson(person1, person3);

        // Case 3: First person is not younger
        testYoungerPerson(person3, person1);

        // Case 4: Objects have the same name
        testSameName(person3, person3Clone);

        // Case 4: Objects do not have the same name
        testSameName(person1, person3);

        // Case 5: Objects have the same age
        testSameAge(person3, person3Clone);

        // Case 5: Objects do not have the same age
        testSameAge(person2, person3);

        /*
         * Testing object initialisation cases where program exists
         * Case 1: Invalid age
         * Case 2: Invalid gender
         * 
         */

        // Create a Person object with an invalid age
        Person person5 = new Person();
        person5.setPerson("Dr. John Edem", -18, "male");

        // Display the attributes of person5 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n\n",
                person5.getName(), person5.getAge(), person5.getGender());

        /*
         * NOTE: To see the effect of person6 object,
         * comment out the person5 object's initialisation and operations.
         *
         * REASON: The program exits if an invalid age is entered.
         *
         */

        // Create a Person object with an invalid gender
        Person person6 = new Person();
        person6.setPerson("John Doe", 67, "Deceased");

        // Display the attributes of person6 object
        System.out.printf("Name: %s\nAge: %d\nGender: %s\n\n",
                person6.getName(), person6.getAge(), person6.getGender());
    }
}
