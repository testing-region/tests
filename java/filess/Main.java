public class Main {
  public static void main(String[] args) {
    FileTree<File> tree = new FileTree<>();
    File file1 = new File("file1");
    File file2 = new File("file2");
    Directory dir3 = new Directory("dir3");
    tree.add(file1);
    tree.add(file2);
    tree.add(dir3);

    dir3.add(new File("file3"));
    dir3.add(new File("file4"));

    Directory dir2 = new Directory("dir2");
    dir3.add(dir2);

    dir2.add(new File("file5"));
    dir2.add(new File("file6"));

    tree.printFileTree();
  }
}

/*
 * If it is null, then the item is not present
 *
 */
