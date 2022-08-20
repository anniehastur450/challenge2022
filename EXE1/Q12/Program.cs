using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q12
{
    class Program
    {
        class Polynomial
        {
            public List<double> coefficients = new List<double>(); // a_i = coefficients[i]
            public double f(double x)
            {
                double ans = 0;
                for (int i = 0; i < coefficients.Count; i++)
                {
                    ans += coefficients[i] * Math.Pow(x, i);
                }
                return ans;
            }
            public Polynomial differentiate()
            {
                Polynomial res = new Polynomial();
                for (int n = 1; n < coefficients.Count; n++)
                {
                    res.coefficients.Add(coefficients[n] * n);
                }
                return res;
            }
        }
        static double findRoot(Polynomial p, Polynomial diff_p, double q_j, double s_j)
        {
            double a;
            a = findRoot0(p, diff_p, (q_j + s_j) / 2);
            if (q_j <= a && a <= s_j) return a;
            a = findRoot0(p, diff_p, q_j);
            if (q_j <= a && a <= s_j) return a;
            a = findRoot0(p, diff_p, s_j);
            if (q_j <= a && a <= s_j) return a;
            return double.NaN;
        }
        static double findRoot0(Polynomial p, Polynomial diff_p, double x_1)
        {
            double error = 0.000_000_001;
            double x_2 = x_1;
            do
            {
                x_1 = x_2;
                x_2 = x_1 - p.f(x_1) / diff_p.f(x_1);
            } while (Math.Abs(x_2 - x_1) > error);
            return x_2;
        }
        static void Q12(List<string> sb)
        {
            // this is a typical newton method question,
            // but i have never touch that before

            // to implement it myself, one gif speak it all:
            // https://commons.wikimedia.org/wiki/File:NewtonIteration_Ani.gif

            int n = int.Parse(sb[0]);
            Polynomial p = new Polynomial();
            for (int i = 0; i <= n; i++)
            {
                p.coefficients.Add(double.Parse(sb[n + 1 - i]));
            }
            Polynomial diff_p = p.differentiate();
            int m = int.Parse(sb[n + 2]);
            for (int j = 0; j < m; j++)
            {
                double q_j = double.Parse(sb[n + 3 + j * 2]);
                double s_j = double.Parse(sb[n + 4 + j * 2]);
                Console.WriteLine(findRoot(p, diff_p, q_j, s_j).ToString("0.000000"));
            }
        }
        static void Main(string[] args)
        {
            string s = null;
            do
            {
                try
                {
                    List<string> sb = new List<string>();
                    while ((s = Console.ReadLine()) != null)
                    {
                        if (s.Length != 0) sb.Add(s);
                        else if (sb.Count != 0) break;
                    }
                    Q12(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            } while (s != null); // should end the program when EOF
        }
    }
}
