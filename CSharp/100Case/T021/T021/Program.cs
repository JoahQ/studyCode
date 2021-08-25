using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T021
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("请输入第一个数：");
            int a = int.Parse(Console.ReadLine());

            Console.WriteLine("请输入第二个数：");
            int b = int.Parse(Console.ReadLine());

            Console.WriteLine("请输入第三个数：");
            int c = int.Parse(Console.ReadLine());

            if (a < b)
            {
                if (b < c)
                    Console.WriteLine("从小到大为：{0},{1},{2}", a, b, c);
                else if (a < c)
                    Console.WriteLine("从小到大为：{0},{1},{2}", a, c, b);
                else
                    Console.WriteLine("从小到大为：{0},{1},{2}", c, a, b);

            }
            else
            {
                if (c < b)
                    Console.WriteLine("从小到大为：{0},{1},{2}", c, b, a);
                else if (a > c)
                    Console.WriteLine("从小到大为：{0},{1},{2}", b, c, a);
                else
                    Console.WriteLine("从小到大为：{0},{1},{2}", b, a, c);

            }
            Console.ReadKey();
            
        }
    }
}
