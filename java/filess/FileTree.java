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

    public T get(String name) {
        return tree.get(name);
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