using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q5
{
    class Program
    {
        static void swap(char[] ch, int a, int b)
        {
            char c = ch[a];
            ch[a] = ch[b];
            ch[b] = c;
        }
        static void do2opt(char[] ch, int index1, int index2)
        {
            if (index1 > index2)
            {
                do2opt(ch, index2, index1);
                return;
            } else {
                for (int i = 0; i < (index2 - index1 + 1) / 2; i++)
                {
                    swap(ch, index1 + i, index2 - i);
                }
            }
        }
        static void Q5(List<string> sb)
        {
            int count = int.Parse(sb[0]);
            string init = "abcdefgha";
            char[] ch = init.ToCharArray();
            for (int i = 1; i <= count; i++)
            {
                int index1 = Array.IndexOf(ch, sb[i][0]);
                int index2 = Array.IndexOf(ch, sb[i][1]);
                do2opt(ch, index1, index2);
            }
            Console.WriteLine(new string(ch));
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
                    Q5(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            } while (s != null); // should end the program when EOF
        }
    }
}
