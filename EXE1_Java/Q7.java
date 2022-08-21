import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Q7 {
    static void Q7(List<String> sb) {
        List<Integer> ints = new ArrayList<>();
        for (String s : String.join(" ", sb).split(" +")) {
            ints.add(Integer.parseInt(s));
        }
        int r = ints.get(0);
        int c = ints.get(1);
        int num = ints.get(2);
        int[][] game = new int[r][c];
        for (int index = 3; index < ints.size(); index += 2) {
            int i = ints.get(index);
            int j = ints.get(index + 1);
            game[i][j] = -1;
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (game[i][j] == -1) {
                    System.out.print("*");
                    continue;
                }
                for (int a = -1; a <= 1; a++) {
                    for (int b = -1; b <= 1; b++) {
                        if (a == 0 && b == 0) continue;
                        int ci = i + a;
                        int cj = j + b;
                        if (ci < 0 || cj < 0 || ci >= r || cj >= c) continue;
                        if (game[ci][cj] != -1) continue;
                        game[i][j]++;
                    }
                }
                System.out.print(game[i][j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        BufferedReader sr = new BufferedReader(new InputStreamReader(System.in));
        String s = null;
        do {
            try {
                List<String> sb = new ArrayList<>();
                while ((s = sr.readLine()) != null) {
                    if (s.length() != 0) sb.add(s);
                    else if (sb.size() != 0) break;
                }
                Q7(sb);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } while (s != null);
    }
}
