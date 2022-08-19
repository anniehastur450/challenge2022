using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Extra_Q3
{
    class Program
    {
        static void Q3(List<string> sb)
        {
            // is regex too cheat?
            MatchCollection a = Regex.Matches(string.Join(" ", sb), "[a-zA-Z’']+");
            SortedSet<string> res = new SortedSet<string>();
            foreach (Match m in a)
            {
                res.Add(m.Value.ToUpperInvariant());
            }
            Console.WriteLine(res.Count);
            foreach (string s in res)
            {
                Console.WriteLine(s);
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
                    Q3(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }
}
