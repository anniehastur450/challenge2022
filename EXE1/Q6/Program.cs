using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q6
{
    class Program
    {
        static int ptr;
        static string s;
        static string[] months = System.Globalization.DateTimeFormatInfo.InvariantInfo.MonthNames;

        class Person
        {
            public int YY;
            public int MM;
            public int DD;
            public int PB;
            public int sss;
            public int G;
            public string id;
            public override string ToString()
            {
                return $"{id} {DD} {months[MM - 1]} {YY} {(G % 2 == 0 ? "Female" : "Male")}";
            }
        }
        class ThenByComparator : IComparer<Person>
        {
            IComparer<Person> first = null;
            IComparer<Person> then = null;
            public ThenByComparator(IComparer<Person> c)
            {
                then = c;
            }
            public ThenByComparator(Comparison<Person> c)
                : this(Comparer<Person>.Create(c)) { }
            public static ThenByComparator of<T>(Func<Person, T> c) where T : IComparable
            {
                return new ThenByComparator((x, y) => c(x).CompareTo(c(y)));
            }
            public ThenByComparator thenBy(IComparer<Person> c)
            {
                ThenByComparator r = new ThenByComparator(c);
                r.first = this;
                return r;
            }
            public int Compare(Person x, Person y)
            {
                int r;
                if (first == null || (r = first.Compare(x, y)) == 0)
                {
                    return then.Compare(x, y);
                }
                return r;
            }
        }

        static string read(int count)
        {
            string res = s.Substring(ptr, count);
            ptr += count;
            return res;
        }

        static int readInt(int count)
        {
            return int.Parse(read(count));
        }

        static void Q6(List<string> sb)
        {
            ptr = 0;
            s = string.Join("", sb).Replace(" ", "").Replace(";", "");
            List<Person> personList = new List<Person>();
            while ('0' <= s[ptr] && s[ptr] <= '9')
            {
                Person p = new Person();
                int st = ptr;
                int YY = readInt(2);
                if (YY > 20) YY += 1900;
                else YY += 2000;
                p.YY = YY;
                p.MM = readInt(2);
                p.DD = readInt(2);
                read(1);
                p.PB = readInt(2);
                read(1);
                p.sss = readInt(3);
                p.G = readInt(1);
                p.id = s.Substring(st, ptr - st);
                personList.Add(p);
            }
            /*
            Birthdate
            BirthYear
            BirthMonth
            BirthDay
            GenderwithMalefirst
            GenderwithFemalefirst
            */
            var dict = new Dictionary<string, ThenByComparator>
            {
                {"Birthdate", ThenByComparator.of(x => x.YY * 10000 + x.MM * 100 + x.DD) },
                {"BirthYear", ThenByComparator.of(x => x.YY) },
                {"BirthMonth", ThenByComparator.of(x => x.MM) },
                {"BirthDay", ThenByComparator.of(x => x.DD) },
                {"GenderwithMalefirst", ThenByComparator.of(x => 1 - x.G % 2) },  // odd first
                {"GenderwithFemalefirst", ThenByComparator.of(x => x.G % 2) },  // even first
            };
            ThenByComparator c = ThenByComparator.of(x => 0); // init
            for (int i = 0; i < 3; i++)
            {
                bool found = false;
                string substr = s.Substring(ptr);
                foreach (string key in dict.Keys)
                {
                    if (substr.StartsWith(key))
                    {
                        c = c.thenBy(dict[key]);
                        ptr += key.Length;
                        found = true;
                        break;
                    }
                }
                if (!found) throw new Exception();
            }
            personList.Sort(c);
            foreach (Person p in personList)
            {
                Console.WriteLine(p.ToString());
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
                    Q6(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }
}
