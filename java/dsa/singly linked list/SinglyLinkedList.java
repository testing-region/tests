/**
 * A node contains data and a reference
 *
 */
class Node<T> {
  T data; // holds the data of a node
  Node<T> next; // holds the pointer to the next node

  public Node(T data) {
    this.data = data;
  }

  /**
   * Check if any two nodes contain the same data
   *
   * @param otherNode the other node to compare with
   * @return whether two nodes have the same data or not
   *
   */
  public boolean equals(Node otherNode) {
    return this.data.equals(otherNode.data);
  }
}

/**
 * Create a singly linked list data structure
 *
 */
public class SinglyLinkedList<T> {
  private int size = 0; // tracks the size of the list
  private Node<T> head; // holds the address of the first node

  /**
   * Insert a node into a linked list
   * 
   * @param data the data to insert into the linked list
   * @param pos  where to insert the data
   */
  public void insert(T data, int pos) {
    Node<T> newNode = new Node<T>(data);

    // if it is for inserting into the first node
    if (pos == 1) {
      newNode.next = head; // set the next node to point to the node head points to
      head = newNode; // set head to the new node, n
      size++; // increase the size of the linked list
      return;
    }

    // if it is for inserting into the end of the linked list
    else if (pos == size + 1) {
      Node<T> current = head; // set the current node to the head

      // set the current node to the end of the linked list
      while (current.next != null) {
        current = current.next;
      }

      // set the current node to point to the new node
      current.next = newNode;
      size++; // increase the size
      return;
    }

    // insert the new node any where between the first and last node
    else {
      Node<T> current = head; // point to the head

      // navigate to the node before the specified one
      for (int i = 1; i < (pos - 1); i++) {
        current = current.next;
      }

      // The new node will be pointed by the node in the position before it.
      newNode.next = current.next;
      current.next = newNode;
      size++;
      return;
    }
  }

  /**
   * Delete a node when given a position
   *
   * @param pos location of a node
   */
  public void delete(int pos) {
    // if the linked list is empty
    if (isEmpty()) {
      return;
    }

    // if the first node is to be removed
    if (pos == 1) {
      head = head.next;
      size--;
      return;
    }

    Node<T> current = head; // set current node to head

    // navigate to the node before the specified one
    for (int i = 1; i < (pos - 1); i++) {
      current = current.next;
    }

    if (pos == size) {
      current.next = null; // if node is at the end of the linked list
    } else {
      current.next = current.next.next; // if the node is any where in-between
    }

    size--; // reduce the size
  }

  /**
   * Check if the linkedlist is empty
   * 
   * @return whether the linkedlist is empty or not
   */
  public boolean isEmpty() {
    return head == null;
  }

  /**
   * Return the data at the specified postion
   * 
   * @param pos postion of the node
   * @return data in the node
   *
   */
  public T get(int pos) {
    if (pos > listSize() || pos < 0) {
      return null; // when there is no node at the specified position
    }

    Node<T> current = head;

    for (int i = 1; i < pos; i++) {
      current = current.next;

    }

    return current.data;
  }

  /**
   * Gets the size of the list
   * 
   * @return the size of the list
   */
  public int listSize() {
    return size;
  }

  /**
   * Gets the position of a node that contains the specified data
   * 
   * @param data the specified data
   * @return the position of the data in the list
   */
  public int positionOf(T data) {
    Node<T> current = head;
    int pos = 1;

    while (current != null) {
      if (current.data.equals(data)) {
        return pos;
      }

      current = current.next;
      pos++;
    }

    return -1; // when the list does not have the data
  }

  /**
   * Display the linked list
   */
  public void display() {
    Node<T> current = head;

    System.out.print("[ ");

    while (current != null) {
      System.out.print(current.data + " ");
      current = current.next;
    }

    System.out.print("]");
    System.out.println();
  }

}
