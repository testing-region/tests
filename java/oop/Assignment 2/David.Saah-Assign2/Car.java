/**
 * This class defines a Car class that represents a car that can hold up to 5
 * people.
 *
 * @author David Saah
 * @version 1.0
 * @since 2023-02-15
 *
 */
public class Car {

    // Initialise Car attributes
    private Person driver;
    private Person frontSeatPassenger;
    private Person backSeatPassenger1;
    private Person backSeatPassenger2;
    private Person backSeatPassenger3;
    private String numberPlate;
    private int occupantsNumber = 0;

    /**
     * A default constructor that sets all the attributes to null
     * 
     */
    public Car() {
        setDriver(null);
        setFrontSeatPassenger(null);
        setBackSeatPassenger1(null);
        setBackSeatPassenger2(null);
        setBackSeatPassenger3(null);
    }

    /**
     * A constructor that sets the driver attribute to the given value but sets the
     * passenger attributes to null
     * 
     */
    public Car(Person driver) {
        setFrontSeatPassenger(null);
        setBackSeatPassenger1(null);
        setBackSeatPassenger2(null);
        setBackSeatPassenger3(null);

        if (driver.getAge() < 18) {
            System.out.println("Error: A driver must be 18 years and above!");
            System.exit(0);
        }
        this.driver = driver;
        occupantsNumber++;
    }

    /**
     * Gets the Person object that represents the driver of the car
     * 
     * @return the driver of the car
     * 
     */
    public Person getDriver() {
        return this.driver;
    }

    /**
     * Gets the Person object that represents the front seat passenger
     * 
     * @return the front seat passenger
     * 
     */
    public Person getFrontSeatPassenger() {
        return this.frontSeatPassenger;
    }

    /**
     * Gets the Person object that represents the first back seat passenger
     * 
     * @return the first back seat passenger
     * 
     */
    public Person getBackSeatPassenger1() {
        return this.backSeatPassenger1;
    }

    /**
     * Gets the Person object that represents the second back seat passenger
     * 
     * @return the second back seat passenger
     * 
     */
    public Person getBackSeatPassenger2() {
        return this.backSeatPassenger1;
    }

    /**
     * Gets the Person object that represents the third back seat passenger
     * 
     * @return the third back seat passenger
     * 
     */
    public Person getBackSeatPassenger3() {
        return this.backSeatPassenger1;
    }

    /**
     * Gets the number plate of the car
     * 
     * @return the number plate details of the car
     * 
     */
    public String getNumberPlate() {
        return this.numberPlate;
    }

    /**
     * Sets the front seat passenger details
     * 
     * @param frontSeatPassenger a person object that represents the front seat
     *                           passenger
     * 
     */
    public void setFrontSeatPassenger(Person frontSeatPassenger) {
        this.frontSeatPassenger = frontSeatPassenger;
        occupantsNumber++;
    }

    /**
     * Sets the first back seat passenger details
     * 
     * @param backSeatPassenger1 a person object representing the first back seat
     *                           passsenger
     * 
     */
    public void setBackSeatPassenger1(Person backSeatPassenger1) {
        this.backSeatPassenger1 = backSeatPassenger1;
        occupantsNumber++;
    }

    /**
     * Sets the second back seat passenger details
     * 
     * @param backSeatPassenger2 a person object representing the second back seat
     *                           passsenger
     * 
     */
    public void setBackSeatPassenger2(Person backSeatPassenger2) {
        this.backSeatPassenger2 = backSeatPassenger2;
        occupantsNumber++;
    }

    /**
     * Sets the third back seat passenger details
     * 
     * @param backSeatPassenger3 a person object representing the third back seat
     *                           passsenger
     * 
     */
    public void setBackSeatPassenger3(Person backSeatPassenger3) {
        this.backSeatPassenger3 = backSeatPassenger3;
        occupantsNumber++;
    }

    /**
     * Sets the number plate details of the car
     * 
     * @param numberPlate the number plate details of the car
     * 
     */
    public void setNumberPlate(String numberPlate) {
        this.numberPlate = numberPlate;
    }

    /**
     * Checks to see if the car has a driver
     * 
     * @return whether the car has a driver or not
     * 
     */
    public boolean hasDriver() {
        return (getDriver() != null);
    }

    /**
     * Checks to see if the car has at least one passenger
     * 
     * @return whether the car has at least one passenger
     * 
     */
    public boolean hasPassengers() {
        return (getFrontSeatPassenger() != null) || (getBackSeatPassenger1() != null)
                || (getBackSeatPassenger2() != null) || (getBackSeatPassenger3() != null);
    }

    /**
     * Checks if the car is empty
     * 
     * @return whether the car is empty
     * 
     */
    public boolean isEmpty() {
        return occupantsNumber == 0;
    }

    /**
     * Checks if the car is full
     * 
     * @return whether the car is full or not
     * 
     */
    public boolean isFull() {
        return occupantsNumber == 5;
    }

    /**
     * Sets the driver of the car
     * Checks if the driver is 18 years and above
     * Replaces the existing driver
     * 
     * @param driver the driver of the car
     * 
     * @return operation state (success/fail)
     * 
     */
    public boolean setDriver(Person driver) {
        if (driver.getAge() < 18) {
            return false;
        }
        this.driver = driver;
        return true;
    }

    /**
     * Tries to put a passenger value
     * 
     * @param passenger
     * 
     * @return whether or not the passenger addition was successful
     * 
     */
    public boolean addPassenger(Person passenger) {
        if (getFrontSeatPassenger() == null) {
            setFrontSeatPassenger(passenger);
            return true;
        } else if (getBackSeatPassenger1() == null) {
            setBackSeatPassenger1(passenger);
            return true;
        } else if (getBackSeatPassenger2() == null) {
            setBackSeatPassenger2(passenger);
            return true;
        } else if (getBackSeatPassenger1() == null) {
            setBackSeatPassenger3(passenger);
            return true;
        } else {
            return false;
        }
    }

    /**
     * Gets the number of occupants in the car
     * 
     * @return the number of occupants in the car
     * 
     */
    public int getNumOccupants() {
        return occupantsNumber;
    }


    /**
     * Lists the information of the riders
     * 
     */
    public void listRiders() {
        // Driver's info
        System.out.printf("Driver's name: %s\n", getDriver().getName());
        System.out.printf("Driver's age: %s\n\n", getDriver().getAge());

        // Passenger 1 info
        System.out.printf("Passenger 1 name: %s\n", getFrontSeatPassenger().getName());
        System.out.printf("Passenger 1 age: %s\n", getFrontSeatPassenger().getAge());
        System.out.println("Sitting position: front\n");

        // Passenger 2 info
        System.out.printf("Passenger 2 name: %s\n", getBackSeatPassenger1().getName());
        System.out.printf("Passenger 2 age: %s\n", getBackSeatPassenger1().getAge());
        System.out.println("Sitting position: back\n");

         // Passenger 3 info
         System.out.printf("Passenger 3 name: %s\n", getBackSeatPassenger2().getName());
         System.out.printf("Passenger 3 age: %s\n", getBackSeatPassenger2().getAge());
         System.out.println("Sitting position: back\n");

          // Passenger 4 info
        System.out.printf("Passenger 4 name: %s\n", getBackSeatPassenger3().getName());
        System.out.printf("Passenger 4 age: %s\n", getBackSeatPassenger3().getAge());
        System.out.println("Sitting position: back\n");
    }

}