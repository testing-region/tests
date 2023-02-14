/**
 * Person
 */
public class Person {

    private String name;
    private int age;
    private String gender;

    /**
     * @param name
     * @param age
     * @param gender
     */
    public Person(String name, int age, String gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @return the age
     */
    public int getAge() {
        return age;
    }

    /**
     * @return the gender
     */
    public String getGender() {
        return gender;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;

        return;
    }

    /**
     * @param age the age to set
     */
    public void setAge(int age) {
        this.age = age;

        return;
    }

    /**
     * @param gender the gender to set
     */
    public void setGender(String gender) {
        this.gender = gender;

        return;
    }

}
