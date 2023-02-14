package Part_2;

public class testIterator {

    public static void main(String[] args) {

        var nums = new NumberGenerator(5);

        nums = new NumberGenerator(10, 0, -1);

        for (Integer num : nums) {
            System.out.println(num);
        }

    }
}
