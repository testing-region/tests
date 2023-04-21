import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Writing {
    public static void main(String[] args) {
        throws IOException {
            String str = "Writing text to a file";
            try {
                FileWriter fw = new FileWriter("output.txt");
                fw.write(str);
                System.out.println("Successfully written");
                fw.close();
            } catch (Exception e) {
                e.getStackTrace();
            }
        }
    }
}
