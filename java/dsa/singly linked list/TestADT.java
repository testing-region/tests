/**
 * TestADT
 */
public class TestADT {

  public static void main(String[] args) {
    SinglyLinkedList list = new SinglyLinkedList();

    list.insert(100, 1);
    list.insert(201, 2);
    list.insert(302, 3);
    list.insert(403, 4);
    list.display();
    list.insert(404, 1);
    list.display();
    list.insert(405, 3);
    list.display();
    list.insert(406, 7);
    list.display();
    list.delete(2);
    list.display();
    list.delete(2);
    list.display();
    list.delete(2);
    list.display();
    System.out.println(list.get(3));
    System.out.println(list.positionOf(403));
  }
}
