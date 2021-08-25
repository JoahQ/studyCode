using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T024
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 1;
            while (true)
            {
                Console.Write(i);
                if (i % 5 == 0)
                    Console.WriteLine();
                else
                    Console.Write("\t");
                if (++i > 20) break;

            }
            Console.ReadLine();
        }
    }
}
