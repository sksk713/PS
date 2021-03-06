import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    static ArrayList<Integer> arr = new ArrayList<>();
    static PriorityQueue<Integer> arr = new PriorityQueue<>(Comparator.reverseOrder());
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x != 0) {
                arr.add(x);
            } else {
                if (arr.isEmpty()) {
                    System.out.println(0);
                } else {
                    System.out.println(arr.poll());
                }
            }
        }
    }
}
