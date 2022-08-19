using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q4
{
    class Program
    {
        static void Q4(List<string> sb, out int v1, out int v2)
        {
            v1 = 0;
            v2 = 0;
            for (int i = 1; i <= 4; i++)
            {
                if (sb[1] == sb[i+1])
                {
                    v1 = i;
                    break;
                }
            }
            if (v1 == 0) return;
            string s = sb[1].Replace(sb[0], "#");
            int count = 0;
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] == '#')
                {
                    count++;
                } else
                {
                    v2 = Math.Max(count, v2);
                    count = 0;
                }
            }
        }
        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    List<string> sb = new List<string>();
                    string s;
                    while (true)
                    {
                        s = Console.ReadLine();
                        if (s.Length != 0) sb.Add(s);
                        else if (sb.Count != 0) break;
                    }
                    int v1;
                    int v2;
                    Q4(sb, out v1, out v2);
                    Console.WriteLine(v1);
                    Console.WriteLine(v2);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }
}
