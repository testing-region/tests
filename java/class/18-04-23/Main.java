import java.util.Arrays;

public class Main {

    public static final String HELP_COMMAND = "help";
    public static final String ADD_COMMAND = "add";
    public static final String SUB_COMMAND = "sub";

    public static void helpMenu() {
        System.out.println("\n  Take arguments from your terminal and use them in your app\n");
        System.out.println("Usage:\n  java Main [command] [argument]\n");
        System.out.println("Available Commands:");
        System.out.println("  help \t\tDisplay this help menu");
        System.out.println("  add \t\tAdd two numbers");
        System.out.println("  sub \t\tSubtract two numbers");
    }

    public static void addNums(double[] arr) {
        System.out.println(Arrays.stream(arr).sum());
    }

    public static void subNums(double num1, double num2) {
        System.out.println(num1 - num2);
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            helpMenu();
            System.exit(0);
        }

        double[] numbers = Arrays.stream(Arrays.copyOfRange(args, 1, args.length)).mapToDouble(Double::parseDouble)
                .toArray();

        switch (args[0]) {
            case HELP_COMMAND:
                helpMenu();
                break;

            case ADD_COMMAND:
                addNums(numbers);
                break;

            case SUB_COMMAND:
                subNums(numbers[0], numbers[1]);
                break;

            default:
                helpMenu();
                System.exit(1);
        }

    }
}
