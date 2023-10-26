/**
 * Deque
 */
public class Deque {
  private int front;
  private int rear;
  private int[] elements;
  private int size = 0;

  public Deque(int size) {
    elements = new int[size];
    front = -1;
    rear = -1;
  }

  public boolean isEmpty() {
    return (front == -1 && rear == -1);
  }

  public int size() {
    return size;
  }

  public boolean isFull() {
    return size() == elements.length;
  }

  public int front() throws Exception {
    if (isEmpty()) {
      throw new Exception("Deque is empty");
    } else {
      return elements[front];
    }
  }

  public int rear() throws Exception {
    if (isEmpty()) {
      throw new Exception("Deque is empty");
    } else {
      return elements[rear];
    }
  }

  public void addFront(int e) throws Exception {
    if (isFull()) {
      throw new Exception("Deque is full");
    }

    if (isEmpty()) {
      front++;
      rear++;
      elements[front] = e;
      size++;
      return;
    }

    for (int i = rear; i >= front; i--) {
      elements[i + 1] = elements[i];
    }

    elements[front] = e;
    rear++;
    size++;
  }

  public void addRear(int e) throws Exception {
    if (isFull()) {
      throw new Exception("Deque is full");
    }

    if (isEmpty()) {
      front++;
      rear++;
      elements[rear] = e;
      size++;
      return;
    }

    rear++;
    elements[rear] = e;
    size++;
  }

  public void removeFront() throws Exception {
    if (isEmpty()) {
      throw new Exception("Deque is empty");
    }

    for (int i = front; i > rear; i--) {
      elements[i] = elements[i + 1];
    }

    size--;
    rear--;
  }

  public static void main(String[] args) {
    Deque nums = new Deque(5);
    try {
      nums.addRear(1);
      nums.addRear(2);
      nums.addRear(3);
      nums.addRear(4);
      nums.removeFront();
      System.out.printf("front: %d\n", nums.front());
      System.out.printf("rear: %d\n", nums.rear());
      System.out.printf("number of elements: %d\n", nums.size());
    } catch (Exception e) {
      System.out.println(e.toString());
    }
  }
}
