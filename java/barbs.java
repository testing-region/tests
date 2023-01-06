import java.util.Scanner;

public class barbs {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is your name?: ");
        String name = scanner.nextLine();
        System.out.printf("I think this is it %s", name);
        scanner.close();
    }
}