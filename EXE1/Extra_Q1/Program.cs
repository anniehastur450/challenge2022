using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Extra_Q1
{
    class Program
    {
        static void Q1(List<string> sb)
        {
            int M = int.Parse(sb[0]);
            int N = int.Parse(sb[1]);
            int P = int.Parse(sb[2]);
            int Q = int.Parse(sb[3]);
            int candy = N * M;
            int ans = 0;
            int paper = 0;
            do
            {
                ans += candy;
                paper += candy;
                candy = paper / P * Q;
                paper %= P;
            } while (candy > 0);
            Console.WriteLine(ans);
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
                    Q1(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            } while (s != null); // should end the program when EOF
        }
    }
}
