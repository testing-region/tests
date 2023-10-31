/**
 * Implement binary search
 * Implement bubblesort
 *
 * Search for ID, name, age, grade, year
 *
 */

class Student {
  String name;
  int id;
  int age;
  int year;
  double grade;

  public Student(String name, int id, int age, int year, double grade) {
    this.name = name;
    this.id = id;
    this.age = age;
    this.year = year;
    this.grade = grade;
  }

}

/**
 * Search
 */
public class Search {

  public static void bubblesort(Student[] students) {
    boolean swapped = true;

    while (swapped) {
      swapped = false;

      for (int i = 0; i < students.length - 1; i++) {
        if (students[i].id > students[i + 1].id) {
          Student temp = students[i];
          students[i] = students[i + 1];
          students[i + 1] = temp;
          swapped = true;
        }
      }
    }
  }

  public static Student binarysearch(Student[] students, int id) throws Exception {
    int low = 0;
    int high = students.length;
    int mid;

    while (low <= high) {
      mid = (int) (low + high) / 2;

      if (students[mid].id == id) {
        return students[mid];
      } else if (students[mid].id < id) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    throw new Exception("Student not found! There is no student this id");
  }

  public static Student binarysearch(Student[] students, String name) throws Exception {
    int low = 0;
    int high = students.length;
    int mid;

    while (low <= high) {
      mid = (int) (low + high) / 2;

      if (students[mid].name.equalsIgnoreCase(name)) {
        return students[mid];
      } else if (students[mid].name.compareToIgnoreCase(name) > 0) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    throw new Exception("Student not found! There is no student this name");
  }

  public static void main(String[] args) {
    Student[] students = {
        new Student("Adjei", 6, 25, 2025, 4.0),
        new Student("David", 1, 20, 2025, 4.0),
        new Student("Nana", 2, 21, 2025, 4.0),
        new Student("Sam", 7, 26, 2025, 4.0),
        new Student("Gideon", 4, 23, 2025, 4.0),
        new Student("Emma", 3, 22, 2025, 4.0),
        new Student("Barbie", 5, 24, 2025, 4.0),
    };

    System.out.println("Unsorted:");

    for (Student student : students) {
      System.out.printf("%d, %s\n", student.id, student.name);
    }

    bubblesort(students);

    System.out.println();
    System.out.println("Sorted:");

    for (Student student : students) {
      System.out.printf("%d, %s\n", student.id, student.name);
    }

    try {
      System.out.println();
      System.out.println("Binary search:");
      Student s1 = binarysearch(students, 1);
      System.out.printf("Searching for id: %d\n", 1);
      System.out.printf("Found: %d, %s\n", s1.id, s1.name);

      System.out.println();

      Student s2 = binarysearch(students, "Gideon");
      System.out.printf("Searching for name: %s\n", "Gideon");
      System.out.printf("Found: %d, %s\n", s2.id, s2.name);
    } catch (Exception e) {
      System.out.println(e);
    }
  }
}
