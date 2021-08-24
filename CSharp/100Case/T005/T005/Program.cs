using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T005
{
    class Program
    {
        static void Main(string[] args)
        {
            float Float = 123.456789f;
            double Double = 123.456789123456789d;
            decimal Decimal1 = 123.456789123456789m;

            Console.WriteLine("单精度浮点型\t{0}", Float);
            Console.WriteLine("双精度浮点型\t{0}", Double);
            Console.WriteLine("高精度浮点型\t{0}", Decimal1);

            Console.ReadLine();
        }
    }
}
