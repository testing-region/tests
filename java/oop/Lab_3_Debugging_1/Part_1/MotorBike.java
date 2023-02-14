public class MotorBike {

    private Person owner;
    private double price;

    /**
     * @param owner
     * @param price
     */
    public MotorBike(Person owner, double price) {
        this.owner = owner;
        this.price = price;
    }

    /**
     * @param price the price to set
     */
    public void setPrice(double price) {
        this.price = price;
    }

    /**
     * @return the owner
     */
    public Person getOwner() {
        return owner;
    }

    public String getOwnersName() {
        return this.owner.getName();

    }

    /**
     * @return the price
     */
    public double getPrice() {
        return price;
    }

    public static void main(String[] args) {

        double suzukiPrice = 1200;
        double harleyPrice = 2000;

        Person girl = new Person("Anisa", 21, "female");
        Person woman = new Person("Mansah", 39, "female");
        Person guy = new Person("Kofi", 25, "male");

        MotorBike bike = new MotorBike(girl, suzukiPrice);

        Person theBoss = bike.getOwner();
        theBoss.setName("Zoey");

        System.out.println("Bike owner: " + bike.getOwnersName());
        System.out.println("Girl: " + girl.getName());
        System.out.println("Bike price: " + bike.getPrice() +
                ", Suzuki price: " + suzukiPrice +
                ", Harley price: " + harleyPrice);

        theBoss = guy;
        bike.setPrice(800);

        girl = woman;
        suzukiPrice = 1500;

        System.out.println("Bike owner: " + bike.getOwnersName());
        System.out.println("Girl: " + girl.getName());
        System.out.println("Bike price: " + bike.getPrice() +
                ", Suzuki price: " + suzukiPrice +
                ", Harley price: " + harleyPrice);

    }
}
