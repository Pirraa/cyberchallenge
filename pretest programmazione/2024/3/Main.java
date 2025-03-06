import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.*;

public class Main {

    public static List<Integer> getRight(List<Integer> S, int D) {
        List<Integer> res = new ArrayList<>(Collections.nCopies(S.size(), 0));
        int j = S.size() - 1;

        for (int i = S.size() - 1; i >= 0; i--) {
            while (j >= 0 && S.get(j) - S.get(i) > D) {
                j--;
            }
            res.set(i, j);
        }
        return res;
    }

    public static List<Integer> getLeft(List<Integer> S, int D) {
        List<Integer> res = new ArrayList<>(Collections.nCopies(S.size(), 0));
        int j = 0;

        for (int i = 0; i < S.size(); i++) {
            while (j < S.size() && S.get(i) - S.get(j) > D) {
                j++;
            }
            res.set(i, j);
        }
        return res;
    }

    public static int findSubsets(int N, int D, List<Integer> S) {
        Collections.sort(S);
        List<Integer> rm = getRight(S, D);
        List<Integer> lm = getLeft(S, D);

        int ans = 0;
        int[] ls = new int[N];
        int[] rs = new int[N];

        for (int i = 0; i < N; i++) {
            ls[i] = i - lm.get(i) + 1;
            if (i > 0) {
                ls[i] = Math.max(ls[i], ls[i - 1]);
            }
        }

        for (int i = N - 1; i >= 0; i--) {
            rs[i] = rm.get(i) - i + 1;

            if (i < N - 1) {
                rs[i] = Math.max(rs[i], rs[i + 1]);
            }
        }

        for (int i = 0; i < N - 1; i++) {
            ans = Math.max(ans, ls[i] + rs[i + 1]);
        }

        return ans;
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Reindirizza l'input da "input.txt"
        System.setIn(new FileInputStream("2024-subset_subset-1_1738062087.txt"));

        // Reindirizza l'output verso "output.txt"
        System.setOut(new PrintStream(new FileOutputStream("output.txt")));
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        while (T-- > 0) {
            int N = sc.nextInt();
            int D = sc.nextInt();

            List<Integer> S = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                S.add(sc.nextInt());
            }

            System.out.println(findSubsets(N, D, S));
        }

        sc.close();
    }
}
