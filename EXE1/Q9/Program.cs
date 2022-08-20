using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q9
{
    class Program
    {
        class Order
        {
            public int minutes = 0;
            public int waitingFood = 0;
            public string human;
            public List<Tuple<string, int>> foods = new List<Tuple<string, int>>();
            public Order(string s)
            {
                string[] s2 = s.Split('#');
                human = s2[0];
                foreach (string sub in s2[1].Split('%'))
                {
                    string[] s3 = sub.Split(':');
                    foods.Add(new Tuple<string, int>(s3[0], int.Parse(s3[1])));
                }
            }
            public bool amIStillWaiting()
            {
                return waitingFood != 0 || foods.Count != 0;
            }
            public void fiveMinutePassed()
            {
                if (amIStillWaiting()) minutes += 5;
            }
        }
        class Cook
        {
            Order fromOrder;
            string currentFood;
            public int remainingCount = 0;
            public void tryToGetFood(List<Order> orders)
            {
                if (remainingCount != 0) return;
                foreach (Order o in orders)
                {
                    if (o.foods.Count != 0)
                    {
                        // from answer ouput we can deduct that cook always choose the food with highest count
                        // (instead of first food)
                        int index = 0;
                        for (int i = 1; i < o.foods.Count; i++)
                        {
                            if (o.foods[i].Item2 > o.foods[index].Item2)
                            {
                                index = i;
                            }
                        }
                        Tuple<string, int> food = o.foods[index];
                        o.foods.RemoveAt(index);
                        currentFood = food.Item1;
                        remainingCount = food.Item2;
                        fromOrder = o;
                        fromOrder.waitingFood += remainingCount;
                        return;
                    }
                }
            }
            public void fiveMinutePassed()
            {
                if (remainingCount != 0)
                {
                    remainingCount--;
                    fromOrder.waitingFood--;
                }
            }
        }
        static bool isThereAnyBodyWaiting(List<Order> orders)
        {
            foreach (Order o in orders)
            {
                if (o.amIStillWaiting()) return true;
            }
            return false;
        }
        static void Q9(List<string> sb)
        {
            string s = string.Join("", sb).Replace(" ", "");
            List<Order> orders = new List<Order>();
            foreach (string sub in s.Split(';'))
            {
                orders.Add(new Order(sub));
            }
            // process order now
            List<Cook> cooks = new List<Cook>();
            for (int i = 0; i < 3; i++) cooks.Add(new Cook());
            while (isThereAnyBodyWaiting(orders))
            {
                foreach (Cook cook in cooks) cook.tryToGetFood(orders);

                foreach (Order o in orders) o.fiveMinutePassed();
                foreach (Cook cook in cooks) cook.fiveMinutePassed();
            }
            foreach (Order o in orders)
            {
                int hr = 10;
                int min = 0;
                min += o.minutes;
                hr += min / 60;
                min %= 60;
                Console.WriteLine($"{o.human} can collect food at {hr:00}:{min:00}");
            }
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
                    Q9(sb);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            } while (s != null); // should end the program when EOF
        }
    }
}
