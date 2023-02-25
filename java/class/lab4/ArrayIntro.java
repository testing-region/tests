/**
 * ArrayIntro
 */
public class ArrayIntro {

    public static void main(String[] args) {
        int[] array1 = { 1, 2, 3, 4, 5 };

        for (int i : array1) {
            System.out.print(i + " ");
        }

        System.out.println();

        int i = 0;
        while (i < array1.length) {
            System.out.print(array1[i] + " ");
            i++;
        }

        System.out.println();
    }
}
