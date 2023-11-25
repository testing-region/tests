import java.io.PrintStream;
import java.util.Collection;
import java.util.HashMap;

class Directory extends File {
  private HashMap<String, File> container;
  private int count;

  public Directory(String name) {
    super(name);
    setIs_dir(true);
    container = new HashMap<>();
    count = 0;
  }

  public void add(File file) {
    container.put(file.getName(), file);
    count++;
  }

  public void delete(String name) {
    container.remove(name);
    count--;
  }

  public File find(String name) {
    return container.get(name);
  }

  public void print() {
    for (File file : container.values()) {
      file.info();
    }
  }

  public PrintStream info() {
    return System.out.format("%-5s %-20s %-3s %s\n", "dir", getModified_time(), count, getName());
  }

  // get all files in this directory
  public Collection<File> getContainer() {
    return container.values();
  }
}