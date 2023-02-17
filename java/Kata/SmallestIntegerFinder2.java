import java.util.Arrays;

public class SmallestIntegerFinder2 {
    public static int findSmallestInt(int[] args) {
        return Arrays.stream(args).boxed().min(Integer::compare).get();
    }
}
