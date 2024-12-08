import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Character> stack = new Stack<Character>();

        int T = Integer.parseInt(sc.nextLine());
        for (int t = 0; t < T; t++) {
            String line = sc.nextLine();
            boolean isVPS = true;
            for (Character c : line.toCharArray()) {
                if (c == '(') stack.push(c);
                else {
                    if (stack.empty()) {
                        isVPS = false;
                        break;
                    } else {
                        stack.pop();
                    }
                }
            }

            if (!stack.empty()) isVPS = false;
            System.out.println(isVPS ? "YES" : "NO");
            stack.clear();
        }
        sc.close();
    }
}