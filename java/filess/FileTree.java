import java.util.TreeMap;

class FileTree<T extends File> {
  private TreeMap<String, T> tree;

  public FileTree() {
    tree = new TreeMap<>();
  }

  public void add(T file) {
    tree.put(file.getName(), file);
  }

  public void remove(String name) {
    tree.remove(name);
  }

  /*
   * Check if a file/directory exists, if it does,
   * return the filepath, else throw an Exception.
   *
   * DFS implementation for finding filepath
   * Traversal method: preorder traversal
   */
  private Result search(File file, String filename) {
    String path = "/";
    boolean ok;

    // check if the file/directory is in the root directory
    if (file.getName().equals(filename)) {
      path += file.getName();
      return new Result(path, true);
    }

    if (file.Is_dir()) {
      path += file.getName();
      for (File f : ((Directory) file).getContainer()) {
        Result result = search(file, filename);
        ok = result.isFound();

        if (ok) {
          path = result.getPath();
          break;
        }
      }
    }

    return new Result("", false);
  }

  public void findPath(String filename) {
    String path = "";
    boolean ok;

    for (File file : tree.values()) {
      Result result = search(file, filename);
      ok = result.isFound();

      if (ok) {
        path = result.getPath();
        break;
      }
    }

    System.out.println(path);
  }

  private void print(File file, String indent) {
    if (indent.length() > 0) {
      System.out.print("|");
    }

    System.out.print(indent + "|-- ");
    System.out.println(file.getName());
    if (file.Is_dir()) {
      for (File f : ((Directory) file).getContainer()) {
        print(f, indent + " ".repeat(4));
      }
    }
  }

  public void printFileTree() {
    for (File file : tree.values()) {
      print(file, "");
    }
  }
}
