using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T015
{
    class Program
    {
        
        static void Main(string[] args)
        {
            do
            {
                Console.WriteLine("请输入第一个数：");
                int Number1 = int.Parse(Console.ReadLine());

                Console.WriteLine("请输入第二个数：");
                int Number2 = int.Parse(Console.ReadLine());

                Console.WriteLine("请输入第三个数：");
                int Number3 = int.Parse(Console.ReadLine());

                int max = Number1 > Number3 ?
                    (Number1 > Number2 ? Number1 : Number2) : //表达式1
                    (Number3 > Number2 ? Number3 : Number2);//表达式2

                Console.WriteLine("{0} {1} {2} 最大值为 {3}", Number1, Number2, Number3, max);

            } while (Console.ReadLine() != "q");

        }


    }
}
