public class Main {

  /**
   * Partitions an array based on the pivot element.
   * It shifts all elements less than the pivot to
   * the left of it. Also, it shifts all elements
   * greater than the pivot point to the right of
   * the pivot.
   *
   * @param arr   the array to be sorted
   * @param start the beginning index
   * @param end   the last index
   *
   * @return the index of the pivot element
   */
  public static int partition(int[] arr, int start, int end) {
    int last = arr[end]; // pick the last element as pivot
    int index = start - 1;

    // swap the elements such that all elements less
    // than the pivot are on the left of the pivot
    // and elements greater than the pivot are on the right
    for (int j = start; j <= end - 1; j++) {
      if (arr[j] <= last) {
        index++;
        int tmp = arr[index];
        arr[index] = arr[j];
        arr[j] = tmp;
      }
    }

    // move the pivot in-between the values less than it
    // and greater than it. It no longer needs to be at
    // end of the array
    int tmp = arr[index + 1];
    arr[index + 1] = arr[end];
    arr[end] = tmp;
    return index + 1;
  }

  /**
   * Performs quicksort operation on the given array
   *
   * @param arr   the array to be sorted
   * @param start the beginning index
   * @param end   the last index
   */
  public static void quicksort(int[] arr, int start, int end) {
    if (start < end) {
      int pivot = partition(arr, start, end); // get pivot position
      quicksort(arr, start, pivot - 1); // recursive call on the left side of the pivot
      quicksort(arr, pivot + 1, end); // recursive call on the right of the pivot
    }
  }

  public static void main(String[] args) {

    int[] nums = { 99, 88, 77, 66, 44, 33, 22, 11 };
    System.out.print("Unsorted: [ ");
    for (int i : nums) {
      System.out.print(i + " ");
    }
    System.out.println("]");

    quicksort(nums, 0, nums.length - 1);

    System.out.print("Sorted: [ ");
    for (int i : nums) {
      System.out.print(i + " ");
    }
    System.out.println("]");

  }
}
