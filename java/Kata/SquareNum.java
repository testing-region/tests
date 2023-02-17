import java.util.Arrays;

public class SquareNum {
    public static int squareSum(int[] n) {
        return Arrays.stream(n).map(x -> x * x).sum();
    }

    public static void main(String[] args) {
        int[] numArray = { 1, 2, 2 };
        System.out.println(squareSum(numArray));
    }
}
