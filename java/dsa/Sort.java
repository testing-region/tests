public class Sort {
  public static void insertionSort(int[] arr) {
    // start with second element
    // first element is assumed to be sorted
    for (int i = 1; i < arr.length; i++) {
      int current = arr[i]; // set the current element
      int j = i - 1; // set the index before the current element

      // this loops runs if j is a valid index
      // and the element at arr[j] > current element
      while (j > -1 && arr[j] > current) {
        arr[j + 1] = arr[j];
        j = j - 1; // reduce the before index by 1 after each iteration
      }

      arr[j + 1] = current;
    }
  }

  public static void selectionSort(int[] arr) {
    // take each index of the array and work on them
    // one by one
    for (int i = 0; i < arr.length; i++) {
      int min = i; // take the element at first index to be the minimum

      // check all the other elements after i and see
      // if any of them is smaller than the one assumed
      // to be the minimum
      for (int j = i + 1; j < arr.length; j++) {
        if (arr[j] < arr[min]) {
          min = j;
        }
      }

      if (min != i) {
        int tmp = arr[i]; // temporary store the value at i
        arr[i] = arr[min]; // set the minimum element at i

        // place the element at i to where the minimum element used to be
        arr[min] = tmp;
      }
    }
  }

  public static void main(String[] args) {
    int[] nums = { 99, 88, 77, 66, 44, 33, 22, 11 };

    System.out.print("Unsorted: [ ");
    for (int i : nums) {
      System.out.print(i + " ");
    }
    System.out.println("]");

    selectionSort(nums);

    System.out.print("Sorted: [ ");
    for (int i : nums) {
      System.out.print(i + " ");
    }
    System.out.println("]");

  }
}
