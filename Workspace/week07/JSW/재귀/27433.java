import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(Factorial(n));
    }
    public static long Factorial(int n) {
        if (n == 0) return 1;
        return n * Factorial(n-1);
    }
}