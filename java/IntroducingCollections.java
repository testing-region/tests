import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class IntroducingCollections {

    public static void main(String[] args) {

        List<String> names = new ArrayList<String>();
        Map<String, Integer> namesAges = new HashMap<String, Integer>();

        readStudentInfo(names, namesAges);
        queryStudentInfo(names, namesAges);

    }

    public static void readStudentInfo(List<String> names,
            Map<String, Integer> namesAges) {

        Scanner input = new Scanner(System.in);

        String moreInput = "Y";
        String name;

        int age;

        while (moreInput.equalsIgnoreCase("Y")) {

            System.out.print("Please enter the name of a student: ");
            name = input.next();
            System.out.print("Now enter the age of a student: ");
            age = input.nextInt();

            names.add(name);
            namesAges.put(name, Integer.valueOf(age));

            System.out.print("Would you like to add more data? (Y/N) ");
            moreInput = input.next();

        }
    }

    public static void queryStudentInfo(List<String> names, Map<String, Integer> namesAges) {

        Scanner input = new Scanner(System.in);

        System.out.println("There are " + names.size() + " students registered: ");

        for (String n : names) {
            System.out.println(n);
        }

        String goAgain = "Y";
        String name;
        Integer age;

        while (goAgain.equalsIgnoreCase("Y")) {

            System.out.print("Enter the name of a student to look up their age: ");
            name = input.next();
            age = namesAges.get(name);
            System.out.println(name + " is " + age + " years old.");

            System.out.print("Would you like to make another query? (Y/N) ");
            goAgain = input.next();
        }

        System.out.println("Goodbye!");
    }
}
