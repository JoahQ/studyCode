using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T046
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "将数字按指定格式输出----格式化字符串";

            Console.WriteLine("请输入一个浮点数字：");
            double number1 = double.Parse(Console.ReadLine());

            Console.WriteLine("输入一个整数字：");
            int number2 = int.Parse(Console.ReadLine());

            Console.WriteLine("常规格式为：\n{0,-16:G6}{1,16:G6}", number1, number2);
            Console.WriteLine();

            Console.WriteLine("货币格式为：\n{0,16:C2}{1,16:C2}", number1, number2);
            Console.WriteLine();

            Console.WriteLine("十进制格式为：\n{0,16}{1,16:D8}", "无", number2);
            Console.WriteLine();

            Console.WriteLine("十六进制格式为：\n{0,16}{1,16:X4}", "无", number2);
            Console.WriteLine();

            Console.WriteLine("科学计数格式为：\n{0,16:E}{1,16:E}", number1, number2);
            Console.WriteLine();

            Console.WriteLine("浮点格式为：\n{0,16:F6}{1,16:F6}", number1, number2);
            Console.WriteLine();

            Console.WriteLine("按千位分隔格式为：\n{0,16:N}{1,16:N}", number1, number2);
            Console.WriteLine();

            Console.ReadLine();

        }
    }
}
