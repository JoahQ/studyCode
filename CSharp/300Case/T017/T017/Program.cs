using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T017
{
    class Program
    {
        static void Main(string[] args)
        {
            do
            {
                Console.WriteLine("请输入一个整数：");
                decimal number = decimal.Parse(Console.ReadLine());
                Console.WriteLine("{0} 的阶乘为 {1}", number, Factorial(number));
            } while (Console.ReadLine() != "q");
        }

        /// <summary>
        /// 计算n的阶乘
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        static decimal Factorial(decimal n)
        {
            if (n == 1) return 1;//将1作为函数返回值

            else return n * Factorial(n - 1);//计算n乘以n-1的阶乘，并作为参数返回值
        }
    }
}
