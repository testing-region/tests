import java.util.Stack;

public class BalanceSym {

  /**
   * Checks whether the symbols, '(' and '{' are balanced.
   * i.e. each opening symbol has its corresponding closing symbol
   * in respective order
   *
   * @param str a string of symbols
   *
   * @return whether the symbols are balanced
   *
   */
  public static boolean isBalanced(String str) {
    // if the first character is a closing symbol, it is not balanced
    if (str.charAt(0) == '}' || str.charAt(0) == ')') {
      return false;
    }

    Stack<Character> lSyms = new Stack<>(); // stack to hold left symbols

    for (char s : str.toCharArray()) {
      if (s == '(' || s == '{') {
        lSyms.push(s); // push left symbols to stack
      }
      // remove left symbol if the immediate right symbol balances it.
      else if (s == ')' && lSyms.peek() == '(') {
        lSyms.pop();
      } else if (s == '}' && lSyms.peek() == '{') {
        lSyms.pop();
      }
    }

    return lSyms.isEmpty(); // if stack is empty, the symbols are balanced
  }

  public static void main(String[] args) {
    String test1 = "{}()((()))()";
    System.out.println(isBalanced(test1));
    String test2 = "{}(((()))()";
    System.out.println(isBalanced(test2));
    String test3 = "}(((()))()";
    System.out.println(isBalanced(test3));
  }
}
