import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Q8 {
    static void Q8_2(List<Double> nums) {
        double prev = 0;
        int count = 0;
        for (Double d : nums) {
            if (d == null) {
                count++;
            } else {
                if (count != 0) {
                    for (int c = 0; c < count; c++) {
                        double res = prev + (d - prev) / (count + 1) * (c + 1);
                        System.out.printf("%.2f\n", res);
                    }
                }
                count = 0;
                prev = d;
            }
        }
    }

    static void Q8(List<String> sb) {
        int count = Integer.parseInt(sb.get(0));
        List<Double> nums = new ArrayList<>();
        for (int i = 1; i <= count; i++) {
            if ("#".equals(sb.get(i))) {
                nums.add(null);
            } else {
                nums.add(Double.parseDouble(sb.get(i)));
            }
        }
        Q8_2(nums);
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
                Q8(sb);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } while (s != null);
    }
}
