import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Q10 {
    static double howMuch0(double[] nums, int i) {
        double sum1 = nums[i + 0] + nums[i + 1] + nums[i + 2];
        sum1 += nums[i + 3] / (sum1 >= 80 ? 2 : 1);
        return sum1;
    }

    static double howMuch(double[] nums) {
        return howMuch0(nums, 0) + howMuch0(nums, 4);
    }
    static void dp(double[] lowest, double[] nums, double[] holder, boolean[] taken, int index) {
        if (index == holder.length) {
            lowest[0] = Math.min(lowest[0], howMuch(holder));
            return;
        }
        for (int i = 0; i < taken.length; i++) {
            if (taken[i]) continue;
            taken[i] = true;
            holder[index] = nums[i];
            dp(lowest, nums, holder, taken, index + 1);
            taken[i] = false;
        }
    }

    static void Q10_2(List<Double> nums0) {
        double[] nums = new double[nums0.size()];
        double[] holder = new double[nums0.size()];
        boolean[] taken = new boolean[nums0.size()];
        for (int i = 0; i < nums0.size(); i++) {
            nums[i] = nums0.get(i);
        }
        double[] lowest = { howMuch(nums) };
        dp(lowest, nums, holder, taken, 0);
        System.out.printf("%.2f\n", lowest[0]);
    }

    static void Q10(List<String> sb) {
        // 8! = 40320, not a big deal
        List<Double> nums = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            nums.add(Double.parseDouble(sb.get(i)));
        }
        Q10_2(nums);
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
                Q10(sb);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } while (s != null);
    }
}
