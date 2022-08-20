using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q11
{
    class Program
    {
        static int intPow(int x, int pow)
        {
            int ret = 1;
            while (pow != 0)
            {
                if ((pow & 1) == 1)
                    ret *= x;
                x *= x;
                pow >>= 1;
            }
            return ret;
        }
        static int map(int a, int b)
        {
            return intPow(2, a) * intPow(3, b);
        }
        static bool f(int[] count, int n, int a, int minB)
        {
            // choose [a] and [minB..(until too large)] for this number
            // and pass [0..a-1] and [b+1] for next number
            // return true/false of "should we continue?"

            int b = minB;
            int k = map(a, b);
            while (k < n)
            {
                for (int nextA = a - 1; nextA >= 0; nextA--)
                {
                    f(count, n - k, nextA, b + 1);
                }
                b++;
                k = map(a, b);
            }
            if (k == n) count[0]++;
            return b != 0;
        }
        static int Q11_2(int n)
        {
            // instead of finding how many ways,
            // we build the number from 0,
            // add one step by one step,
            // until the number is larger than the target

            // condition 1 is important: None of the summands can divide any of the other summands.

            // consider 2^a * 3^b and 2^c * 3^d
            // if a >= c && b >= d, then condition 1 must violate
            // question: is diff set of (a, b) map to unique numer? ans: yes
            int[] count = new int[1];
            int a = 0;
            while (f(count, n, a, 0)) a++;

            return count[0];
        }
        static void Q11(List<string> sb)
        {
            Console.WriteLine(Q11_2(int.Parse(sb[0])));
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
                    Q11(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            } while (s != null); // should end the program when EOF
        }
    }
}
