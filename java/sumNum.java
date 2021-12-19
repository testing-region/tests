public class sumNum {
    public static void main(String[] args) {
        int num, sum = 0;
        System.out.print("Enter a non-zero positive integer: ");

        // get input from user
        num = getInt();
        for (int i = 1; i <= num; i++) {
            sum = sum + i;
        }
        System.out.println("The sum of all integers between 1 and " + num + " is " + sum);
    }

    // function to get integer from user
    public static int getInt() {
        int num = 0;
        try {
            num = Integer.parseInt(System.console().readLine());
        } catch (NumberFormatException e) {
            // print error message
            System.out.println("Invalid input. Please enter a non-zero positive integer.");
            num = getInt();
        }
        return num;
    }
}