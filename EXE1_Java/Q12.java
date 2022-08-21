import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Q12 {
    static class Polynomial {
        List<Double> coefficients = new ArrayList<>(); // a_i = coefficients[i]

        double f(double x) {
            double ans = 0;
            for (int i = 0; i < coefficients.size(); i++) {
                ans += coefficients.get(i) * Math.pow(x, i);
            }
            return ans;
        }

        Polynomial differentiate() {
            Polynomial res = new Polynomial();
            for (int n = 1; n < coefficients.size(); n++) {
                res.coefficients.add(coefficients.get(n) * n);
            }
            return res;
        }
    }

    static double findRoot(Polynomial p, Polynomial diff_p, double q_j, double s_j) {
        double a;
        a = findRoot0(p, diff_p, (q_j + s_j) / 2);
        if (q_j <= a && a <= s_j) return a;
        a = findRoot0(p, diff_p, q_j);
        if (q_j <= a && a <= s_j) return a;
        a = findRoot0(p, diff_p, s_j);
        if (q_j <= a && a <= s_j) return a;
        return Double.NaN;
    }

    static double findRoot0(Polynomial p, Polynomial diff_p, double x_1) {
        double error = 0.000_000_001;
        double x_2 = x_1;
        do {
            x_1 = x_2;
            x_2 = x_1 - p.f(x_1) / diff_p.f(x_1);
        } while (Math.abs(x_2 - x_1) > error);
        return x_2;
    }

    static void Q12(List<String> sb) {
        // this is a typical newton method question,
        // but i have never touch that before

        // to implement it myself, one gif speak it all:
        // https://commons.wikimedia.org/wiki/File:NewtonIteration_Ani.gif

        int n = Integer.parseInt(sb.get(0));
        Polynomial p = new Polynomial();
        for (int i = 0; i <= n; i++) {
            p.coefficients.add(Double.parseDouble(sb.get(n + 1 - i)));
        }
        Polynomial diff_p = p.differentiate();
        int m = Integer.parseInt(sb.get(n + 2));
        for (int j = 0; j < m; j++) {
            double q_j = Double.parseDouble(sb.get(n + 3 + j * 2));
            double s_j = Double.parseDouble(sb.get(n + 4 + j * 2));
            System.out.printf("%.6f\n", findRoot(p, diff_p, q_j, s_j));
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
                Q12(sb);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } while (s != null);
    }
}
