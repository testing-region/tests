/**
 * This program tests the Car class.
 *
 * @author David Saah
 * @version 1.0
 * @since 2023-02-15
 *
 */
public class TestCar {

    public static void testHasPassengers(Car car) {
        if (car.hasPassengers()) {
            System.out.println("The car has at least one passenger\n");
        } else {
            System.out.println("The car has no passengers\n");
        }
    }

    public static void testIsEmpty(Car car) {
        if (car.isEmpty()) {
            System.out.println("The car is empty\n");
        } else {
            System.out.println("The car is not empty\n");
        }
    }

    public static void main(String[] args) {

        /*
         * Cannot test for values with null
         * Drawback: Java Null pointer exception
         * 
         */
        // Car car1 = new Car();
        // System.out.println(car1.getDriver());

        /*
         * NOTE: To see the output when a driver's age is less than the required,
         * Uncomment the block of code below
         * 
         * REASON: Program exits if driver's age is less than 18 years
         * 
         */
        // Person driver1 = new Person("Kofi", 2, "male");
        // Car car2 = new Car(driver1);
        // System.err.println(car2.getDriver());

        /*
         * NOTE: To see output when a car has no driver,
         * uncomment the block of code below
         * 
         * REASON: Program exits when the driver is not set.
         * CAUSE: Driver's age is not greater than 18
         * 
         */
        // Person driver3 = new Person("Kwame", 3, "male");
        // Car car3 = new Car(driver3);
        // System.out.println(car3.hasDriver());

        /*
         * NOTE: Cannot test `hasDriver` method
         * Drawback: Java Null pointer exception
         * 
         */
        // Car car4 = new Car();
        // System.out.println(car4.hasDriver());

        // Create driver and passenger objects
        Person driver = new Person("Kwame", 33, "male");
        Person passeger1 = new Person("Kojo", 12, "male");
        Person passeger2 = new Person("Abena", 22, "female");
        Person passeger3 = new Person("Adjoa", 27, "female");
        Person passeger4 = new Person("Fiifi", 42, "male");

        // Initialiase car5 with a driver (with passengers)
        Car car5 = new Car(driver);

        // Initialise car6 (with no passengers)
        Car car6 = new Car(driver);

        // Initialise car7 as an empty car
        // Car car7 = new Car();

        // Check if the car5 has a driver
        if (car5.hasDriver()) {
            System.out.println("The car has a driver\n");
        } else {
            System.out.println("The car has no driver\n");
        }

        // Add passengers to the car5
        car5.setFrontSeatPassenger(passeger4);
        car5.setBackSeatPassenger1(passeger1);
        car5.setBackSeatPassenger2(passeger3);
        car5.setBackSeatPassenger3(passeger2);

        /*
         * Test if cars have passengers.
         * Case 1: No passengers
         * Case 2: At least one passenger
         * 
         */

        // Case 1: Has no passengers
        testHasPassengers(car6);

        // Case 2: Has paasengers
        testHasPassengers(car5);

        /*
         * Test if a car is empty.
         * Case 1: Car is empty
         * Case 2: Car is not empty
         * 
         */

        /*
         * NOTE: Cannot test if car is empty
         * Drawback: Java Null pointer exception
         * 
         */
        // Case 1: Car is empty
        // testIsEmpty(car7);

        // Case 2: Car in not empty
        testIsEmpty(car5);

        // list all the riders
        car5.listRiders();

        
    }
}