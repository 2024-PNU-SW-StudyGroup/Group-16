
import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        LinkedList<Integer> queue = new LinkedList<>();
        int N = Integer.parseInt(br.readLine());
        int cache = 0;
        for (int n = 0; n < N; n++) {
            String[] line = br.readLine().split(" ");
            switch (line[0]) {
                case "push":
                    cache = Integer.parseInt(line[1]);
                    queue.add(cache);
                    break;
                case "pop":
                    sb.append(!queue.isEmpty() ? queue.poll() : -1).append('\n');
                    break;

                case "size":
                    sb.append(queue.size()).append('\n');
                    break;

                case "empty":
                    sb.append(queue.isEmpty() ? 1 : 0).append('\n');
                    break;

                case "front":
                    sb.append(queue.isEmpty() ? -1 : queue.peek()).append('\n');
                    break;

                case "back":
                    sb.append(queue.isEmpty() ? -1 : cache).append('\n');
                    break;
                default:
                    break;
            }
        }

        bw.write(sb.toString());
        br.close();
        bw.close();
    }
}