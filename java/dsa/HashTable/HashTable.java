/*
 * Implement a Hash Table using the Algorithms discussed. The
 * Entry objewct can have a student ID as key and their grade
 * as Value.
 *
 */

/**
 * HashTable
 */
public class HashTable {
  private int capacity; // capacity of the hashtable
  private int[] table; // holds hashtable values
  private int size; // tracks the number of elements in the table

  /**
   * Constructor
   */
  public HashTable(int initialCapacity) {
    createTable(initialCapacity);
  }

  /**
   * Initialises a hash table
   *
   * @param initialCapacity specifies table capacity
   *
   */
  private void createTable(int initialCapacity) {
    capacity = initialCapacity;
    table = new int[capacity];
    size = 0;
  }

  /**
   * Checks whether the HashTable is empty
   *
   * @return whether the HashTable is empty
   *
   */
  public boolean isEmpty() {
    return size == 0;
  }

  /**
   * Gets the table length
   *
   * @return the number of elements in the table
   *
   */
  public int tableLength() {
    return size;
  }

  /**
   * Returns the hash value of a function
   * 
   * @param key the value to be hashed
   *
   * @return the hashed key
   *
   */
  private int primaryHash(int key) {
    return key % capacity;
  }

  /**
   * A secondary hash function
   *
   * @param key the value to be hashed
   * 
   * @return a non-zero and different hash
   */
  private int secondaryHash(int key) {
    return 17 - (key % 17);
  }

  public void insert(int key, int value) throws Exception {
    if (tableLength() == capacity) {
      throw new Exception("Hashtable is full");
    }

    int newIndex = -1;
    int primaryIndex = primaryHash(key);
    int secondaryIndex = secondaryHash(key);

    for (int i = 0; i < capacity; i++) {
      int index = ((primaryIndex + 1) * secondaryIndex) % capacity;

      if (table[index] == 0) {
        newIndex = index;
        break;
      }
    }
  }
}
