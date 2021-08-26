using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T029
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("请输入字符串：");
            string str = Console.ReadLine();

            foreach (char c in str)
            {
                Console.WriteLine(c);
            }
            Console.ReadLine();
        }
    }
}
