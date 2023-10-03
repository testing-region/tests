/**
 * A node contains data and a reference
 *
 */
class Node {
  int data; // holds the data of a node
  Node next; // holds the pointer to the next node
  Node prev; // holds the pointer to the prev node

  public Node(int data) {
    this.data = data;
  }
}

/**
 * Create a singly linked list data structure
 *
 */
public class DoublyLinkedList {
  private int size = 0; // tracks the size of the list
  private Node head; // holds the address of the first node
  private Node tail; // holds the address of the last node

  /**
   * Insert a node into a linked list
   * 
   * @param data the data to insert into the linked list
   * @param pos  where to insert the data
   */
  public void insert(int data, int pos) {
    Node newNode = new Node(data);

    // if it is for inserting into the first node
    if (pos == 1) {
      newNode.next = head; // set the next node to point to the head
      newNode.prev = null; // set the previous node to point to null
      head = newNode; // set head to the new node
      size++; // increase the size of the linked list

      // if the size is 1, head = tail
      if (listSize() == 1) {
        tail = newNode;
      }

      return;
    }

    // if it is for inserting into the end of the linked list
    else if (pos == listSize() + 1) {
      newNode.prev = tail; // set the prev node to point to the end node
      tail.next = newNode; // set last node as newNode

      tail = newNode;
      size++; // increase the size
      return;
    }

    // insert the new node any where between the first and last node
    else {
      Node current = head; // point to the head

      // navigate to the node before the specified one
      for (int i = 1; i < (pos - 1); i++) {
        current = current.next;
      }

      newNode.next = current.next;
      newNode.prev = current;

      current.next.prev = newNode;
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

    // if the last node is to be removed
    else if (pos == listSize()) {
      tail = tail.prev;
      tail.next = null;
      size--;
      return;
    }

    // when deleting from anywhere in between
    else {
      Node current = head; // set current node to head

      // navigate to the node before the specified one
      for (int i = 1; i < (pos - 1); i++) {
        current = current.next;
      }

      current.next = current.next.next;
      current.next.prev = current;
      size--; // reduce the size
      return;
    }

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
  public int get(int pos) {
    Node current = head;

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
  public int positionOf(int data) {
    Node current = head;
    int pos = 0;

    for (int i = 1; i <= listSize(); i++) {
      if (current.data == data) {
        pos = i;
        break;
      }

      current = current.next;
    }

    return pos;
  }

  /**
   * Display the linked list
   */
  public void display() {
    Node current = head;

    System.out.print("[ ");

    while (current != null) {
      System.out.print(current.data + " ");
      current = current.next;
    }

    System.out.print("]");
    System.out.println();
  }

}
