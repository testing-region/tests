/**
 * This class defines a Person class with 3 attributes.
 *
 * @author David Saah
 * @version 1.0
 * @since 2023-02-06
 *
 */
public class Person {

    // Initialise Person attributes
    private String name;
    private byte age; // A person's age is rarely greater than 127 years.
    private String gender;

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
    public byte getAge() {
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
    public void setAge(byte age) {
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
        if (gender.equalsIgnoreCase("male") || gender.equalsIgnoreCase("female")) {
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
    public void setPerson(String name, byte age, String gender) {
        setName(name);
        setAge(age);
        setGender(gender);
    }
}
