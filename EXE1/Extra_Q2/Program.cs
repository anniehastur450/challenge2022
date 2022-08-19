using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Extra_Q2
{
    class Program
    {
        static Dictionary<string, double> factors = new Dictionary<string, double>
        {
            {"American Beech", 6},
            {"Basswood", 3},
            {"Common Horsechestnut", 8},
            {"Dogwood", 7},
            {"European White Birch", 5},
            {"White Fir", 7.5},
        };
        static void Q2(List<string> sb)
        {
            int N;
            try
            {
                N = int.Parse(sb[0]);
                if (N <= 0) throw new Exception();
            }
            catch
            {
                Console.WriteLine("You must specify a positive integer number for the number of trees!");
                return;
            }
            for (int i = 0; i < N; i++)
            {
                double circum = double.Parse(sb[1 + i * 2]);
                string treeName = sb[2 + i * 2];
                if (circum <= 0)
                {
                    Console.WriteLine($"The circumference for {treeName} must be greater than 0!");
                    continue;
                }
                if (factors.ContainsKey(treeName))
                {
                    double DBH = circum / 3.141592;
                    double age = DBH * factors[treeName];
                    Console.WriteLine($"{treeName} : {circum:0.0} : {age:0.0}");
                } else
                {
                    Console.WriteLine("Species entered is not available!");
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
                    Q2(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }
}
