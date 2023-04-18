/**
 *
 * Tests out some basic examples of collections in java
 *
 */
public class Main {
    public static void main(String[] args) {

    }
}

/**
 * Drawable
 */
public interface Drawable {
    void draw();
}

/**
 * Circle
 */
public class Circle implements Drawable {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public void draw() {
        System.out.println("Drawing a circle with radius: " + radius);
    }
}
