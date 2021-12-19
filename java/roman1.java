public class roman {
    int num = 0;
    String romanNum = "";
    public static void main(String[] args) {
        roman r = new roman();
        r.getInt();
        r.checkNum();
        r.convertNum();
        System.out.println(r.romanNum);
    }

    public void getInt() {
        try {
            System.out.print("Enter a non-zero positive integer: ");
            num = Integer.parseInt(System.console().readLine());
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a non-zero positive integer.");
            getInt();
        }
    }

    public void checkNum() {
        if (num < 1 || num > 10) {
            System.out.println("Invalid input. Please enter a non-zero positive integer.");
        }
    }

    public void convertNum() {
        if (num == 1) {
            romanNum = "I";
        } else if (num == 2) {
            romanNum = "II";
        } else if (num == 3) {
            romanNum = "III";
        } else if (num == 4) {
            romanNum = "IV";
        } else if (num == 5) {
            romanNum = "V";
        } else if (num == 6) {
            romanNum = "VI";
        } else if (num == 7) {
            romanNum = "VII";
        } else if (num == 8) {
            romanNum = "VIII";
        } else if (num == 9) {
            romanNum = "IX";
        } else if (num == 10) {
            romanNum = "X";
        }
    }

    public String getRomanNum() {
        return romanNum;
    }


}