import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while (!(line = br.readLine()).equals(".")) {
            sb.append(isVPS(line) ? "yes\n" : "no\n");
        }
        System.out.println(sb.toString());
        br.close();
    }

    public static HashMap<Character, Character> dict = new HashMap<Character, Character>() {
        {
            put('(', ')');
            put('[', ']');
        }
    };

    public static boolean isVPS(String str) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : str.toCharArray()) {
            if (c == '(' || c == '[') {
                stack.push(c);
            }
            else if (c == ')' || c == ']') {
                if (stack.isEmpty() || dict.get(stack.pop()) != c) {
                    return false;
                }

            }
        }

        return stack.isEmpty();
    }
}