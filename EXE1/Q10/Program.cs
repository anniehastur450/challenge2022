using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q10
{
    class Program
    {
        static double lowest;
        static double howMuch0(double[] nums, int i)
        {
            double sum1 = nums[i + 0] + nums[i + 1] + nums[i + 2];
            sum1 += nums[i + 3] / (sum1 >= 80 ? 2 : 1);
            return sum1;
        }
        static double howMuch(double[] nums)
        {
            return howMuch0(nums, 0) + howMuch0(nums, 4);
        }
        static void dp(List<double> nums, double[] holder, bool[] taken, int index)
        {
            if (index == holder.Length)
            {
                lowest = Math.Min(lowest, howMuch(holder));
                return;
            }
            for (int i = 0; i < taken.Length; i++)
            {
                if (taken[i]) continue;
                taken[i] = true;
                holder[index] = nums[i];
                dp(nums, holder, taken, index + 1);
                taken[i] = false;
            }
        }
        static void Q10_2(List<double> nums)
        {
            lowest = howMuch(nums.ToArray());
            double[] holder = new double[nums.Count];
            bool[] taken = new bool[nums.Count];
            dp(nums, holder, taken, 0);
            Console.WriteLine(lowest.ToString("0.00"));
        }
        static void Q10(List<string> sb)
        {
            // 8! = 40320, not a big deal
            List<double> nums = new List<double>();
            for (int i = 0; i < 8; i++)
            {
                nums.Add(double.Parse(sb[i]));
            }
            Q10_2(nums);
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
                    Q10(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }
}
