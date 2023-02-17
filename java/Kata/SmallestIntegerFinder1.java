import java.util.stream.IntStream;

public class SmallestIntegerFinder1 {
    public static int findSmallestInt(int[] args) {
        return IntStream.of(args).min().getAsInt();
    }
}
