package dsa;

/**
 * A node contains data and a reference
 *
 */
class Node {
  int data; // holds the data of a node
  Node next; // holds the pointer to the next node

  public Node(int data) {
    this.data = data;
    this.next = null;
  }
}

/**
 * Create a singly linked list data structure
 *
 */
public class SinglyLinkedList {
  private int size = 0; // tracks the size of the list
  private Node head; // holds the address of the first node

  public SinglyLinkedList() {
    this.head = null;
  }

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
      newNode.next = this.head; // set the next node to point to the node head points to
      this.head = newNode; // set head to the new node, n
      size++; // increase the size of the linked list
      return;
    }

    // if it is for inserting into the end of the linked list
    else if (pos == size + 1) {
      Node current = head; // set the current node to the head

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
      int count = 1; // track movement in the linked list
      Node current = head; // point to the head

      // The new node will be pointed by the node in the position before it.
      while (count < (pos - 1)) {
        current = current.next;
        count++;
      }

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
    if (head == null) {
      return;
    }
    // if the first node is to be removed
    else if (pos == 1) {
      head = head.next;
      size--;
      return;
    }

    // if node is at the end of the linked list
    else if (pos == size) {
      Node current = head; // set current node to head
      int counter = 1; // track the movement in the linked list

      while (count < (pos - 1)) {
        current = current.next;
        count++;
      }

      current.next = null;
      size--;
      return;
    }

    // if the node is any where in-between
    else {
      Node current = head;
      int count = 1;

      while (count < (pos - 1)) {
        current = current.next;
        count++;
      }

      current.next = current.next.next;
      size--;
      return;
    }
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
