public class search {
  public static int jumpSearch(int[] nums, int target) {
    int m = (int) Math.pow(nums.length, 0.5);
    int i = 0;

    while (i < nums.length) {
      if (nums[i] == target) {
        return i;
      } else if (nums[i] < target) {
        i += m;
      } else {
        break;
      }
    }

    if (i >= nums.length) {
      i -= m;
    }

    for (int j = 0; j < nums.length - 1; j++) {
      if (nums[j] == target) {
        return j;
      }
    }

    return -1;
  }

  public static int exponentialSearch(int[] nums, int target) {
    if (nums[0] == target) {
      return 0;
    }

    int i = 1;

    while (i < nums.length && nums[i] <= target) {
      i *= 2;
    }

    return -1;
  }

  public static void main(String[] args) {
    int[] nums = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    System.out.println(jumpSearch(nums, 7));
  }
}
