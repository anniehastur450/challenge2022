using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q7
{
    class Program
    {
        static void Q7(List<string> sb)
        {
            string[] firstLine = sb[0].Split(' ');
            int r = int.Parse(firstLine[0]);
            int c = int.Parse(firstLine[1]);
            int num = int.Parse(firstLine[2]);
            int[,] game = new int[r, c];
            for (int n = 1; n <= num; n++)
            {
                string[] line = sb[n].Split(' ');
                int i = int.Parse(line[0]);
                int j = int.Parse(line[1]);
                game[i, j] = -1;
            }
            for (int i = 0; i < r; i++)
            {
                for (int j = 0; j < c; j++)
                {
                    if (game[i, j] == -1)
                    {
                        Console.Write('*');
                        continue;
                    }
                    for (int a = -1; a <= 1; a++)
                    {
                        for (int b = -1; b <= 1; b++)
                        {
                            if (a == 0 && b == 0) continue;
                            int ci = i + a;
                            int cj = j + b;
                            if (ci < 0 || cj < 0 || ci >= r || cj >= c) continue;
                            if (game[ci, cj] != -1) continue;
                            game[i, j]++;
                        }
                    }
                    Console.Write(game[i, j]);
                }
                Console.WriteLine();
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
                    Q7(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }
}
