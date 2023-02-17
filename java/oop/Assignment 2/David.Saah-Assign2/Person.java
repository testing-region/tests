
// import needed packages
import java.util.Random;
import java.util.Arrays;

/**
 * This class defines a Person class with 3 attributes.
 *
 * @author David Saah
 * @version 2.0
 * @since 2023-02-06
 *
 */
public class Person {

    // Initialise Person attributes
    private String name;
    private int age;
    private String gender;
    private String[] genderTypes = { "male", "female" };

    /**
     * Person constructor
     * 
     * Sets default values to field names: name, age, gender
     * Randomly assigns gender of new object
     * 
     */
    public Person() {
        // create random object
        Random random = new Random();

        // randomly select an index in genderTypes
        int option = random.nextInt(getGenderTypes().length);

        setName("No name yet");
        setAge(0);
        setGender(getGenderTypes()[option]);
    }

    /**
     * Person constructor with parameters
     * 
     * Sets the field names of person object with given values
     * 
     * @param name   the name of a person
     * @param age    the age of the person
     * @param gender the gender of the person, whether "male" or "female"
     */
    public Person(String name, int age, String gender) {
        setPerson(name, age, gender);
    }

    /**
     * Gets the genderTypes array
     *
     * @return a list of gender types
     *
     */
    public String[] getGenderTypes() {
        return this.genderTypes;
    }

    /**
     * Gets the name of the person
     *
     * @return the name of the person
     *
     */
    public String getName() {
        return name;
    }

    /**
     * Gets the age of the person
     *
     * @return the age of the person
     *
     */
    public int getAge() {
        return age;
    }

    /**
     * Gets the gender of the person
     *
     * @return the gender of the person
     *
     */
    public String getGender() {
        return gender;
    }

    /**
     * Sets the name of the person
     *
     * @param name the name of a person
     *
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Sets the age of the person if the value chosen is not negative.
     * Displays an error message if the age chosen is negative.
     * Exits the program after displaying an error message.
     *
     * @param age the age chosen
     *
     */
    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        } else {
            System.out.println("Error: The age entered is negative!");
            System.exit(0);
        }
    }

    /**
     * Sets the gender of the person.
     * For simplicity, valid values for gender are "male" and "female".
     * It checks if an invalid value for gender is given.
     * Displays an error message if the chosen gender is invalid.
     * Exits the program after displaying an error message.
     *
     * @param gender the gender of a person, whether "male" or "female"
     *
     */
    public void setGender(String gender) {
        // Check if gender entered is valid
        boolean isValidGender = Arrays.stream(getGenderTypes())
                .anyMatch(gender::equalsIgnoreCase);

        if (isValidGender) {
            this.gender = gender;
        } else {
            System.out.println("Error: The gender status is not found in our database!");
            System.exit(0);
        }
    }

    /**
     * Sets all the attributes of a person: name, age and gender.
     *
     * @param name   the name of the person
     * @param age    the age of the person
     * @param gender the gender of the person, whether "male" or "female"
     *
     */
    public void setPerson(String name, int age, String gender) {
        setName(name);
        setAge(age);
        setGender(gender);
    }

    /**
     * Checks if two person objects have the same name
     * 
     * @param otherPerson another person object
     * @return whether the two person objects have the same name
     */
    public boolean isSameName(Person otherPerson) {
        return getName().equals(otherPerson.getName());
    }

    /**
     * Checks if two person objects have the same age
     * 
     * @param otherPerson another person object
     * @return whether the two person objects have the same age
     */
    public boolean isSameAge(Person otherPerson) {
        return getAge() == otherPerson.getAge();
    }

    /**
     * Checks if two person objects are equal
     * i.e. they have the same name and age
     * 
     * @param otherPerson another person object
     * 
     * @return whether the person objects are equal or not
     * 
     */
    public boolean equals(Person otherPerson) {
        return isSameName(otherPerson) && isSameAge(otherPerson);
    }

    /**
     * Checks if a person object is older than the other
     * 
     * @param otherPerson another person object
     * @return whether a person is older than the other
     */
    public boolean isOlder(Person otherPerson) {
        return getAge() > otherPerson.getAge();
    }

    /**
     * Checks if a person object is younger than the other
     * 
     * @param otherPerson another person object
     * @return whether a person is younger than the other
     */
    public boolean isYounger(Person otherPerson) {
        return !isOlder(otherPerson);
    }
}
