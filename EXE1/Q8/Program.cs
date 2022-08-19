using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q8
{
    class Program
    {
        static void Q8_2(List<double?> nums)
        {
            double prev = 0;
            int count = 0;
            foreach (double? d in nums)
            {
                if (d == null)
                {
                    count++;
                }
                else
                {
                    if (count != 0)
                    {
                        for (int c = 0; c < count; c++)
                        {
                            double res = (double) (prev + (d - prev) / (count + 1) * (c + 1));
                            Console.WriteLine(res.ToString("0.00"));
                        }
                    }
                    count = 0;
                    prev = (double) d;
                }
            }
        }
        static void Q8(List<string> sb)
        {
            int count = int.Parse(sb[0]);
            List<double?> nums = new List<double?>();
            for (int i = 1; i <= count; i++)
            {
                if (sb[i] == "#")
                {
                    nums.Add(null);
                }
                else
                {
                    nums.Add(double.Parse(sb[i]));
                }
            }
            Q8_2(nums);
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
                    Q8(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }
}
