import java.io.PrintStream;
import java.time.LocalDate;
import java.time.LocalTime;

class File {
  private String modified_time;
  private String created_time;
  private String name;
  private boolean is_dir;

  public File(String name) {
    this.name = name;
    this.is_dir = false;
    this.created_time = getDateTime();
    this.modified_time = getDateTime();
  }

  private String getDateTime() {
    String time = LocalTime.now().toString();
    time = time.substring(0, time.indexOf("."));
    return LocalDate.now().toString() + " " + time;
  }

  public String getModified_time() {
    return modified_time;
  }

  public void upModified_time() {
    this.modified_time = getDateTime();
  }

  public String getCreated_time() {
    return created_time;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public boolean Is_dir() {
    return is_dir;
  }

  protected void setIs_dir(boolean is_dir) {
    this.is_dir = is_dir;
  }

  public PrintStream info() {
    return System.out.format("%-5s %-20s %-3s %s\n", "file", modified_time, "", name);
    }
}
