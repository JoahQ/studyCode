using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T016
{
    class Program
    {
        static void Main(string[] args)
        {
            do
            {
                Console.WriteLine("请输入一个数：");
                int number1 = int.Parse(Console.ReadLine());

                Console.WriteLine("请输入第二个数：");
                int number2 = int.Parse(Console.ReadLine());

                Program.Exchangle(ref number1, ref number2);

                Console.WriteLine("将两个数交换...");
                Console.WriteLine("第一个数等于：{0}, 第二个数等于：{1}", number1, number2);
                
            } while (Console.ReadLine() != "q");
        }

        /// <summary>
        /// 参数面前的ref关键字表示该参数为值类型的引用专递。
        /// 所谓引用传递，即将数值本身传递到函数体内，
        /// 在函数中对该参数的修改会造成对数值本身的修改。
        /// </summary>
        /// <param name="number1"></param>
        /// <param name="number2"></param>
        static void Exchangle(ref int number1, ref int number2)
        {

            int temp = number2;
            number2 = number1;
            number1 = temp;

        }
    }
}
