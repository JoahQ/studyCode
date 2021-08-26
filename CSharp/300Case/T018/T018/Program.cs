using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T018
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("请输入第一个数：");
            int number1 = int.Parse(Console.ReadLine());
            Console.WriteLine("请输入第二个数：");
            int number2 = int.Parse(Console.ReadLine());
            Console.WriteLine("请输入第三个数：");
            int number3 = int.Parse(Console.ReadLine());

            Program p = new Program();

            int resul;//存储三个数相乘的结果
            p.GetMultResult(out resul, number1, number2, number3);

            Console.WriteLine("{0} * {1} * {2} = {3}", number1, number2, number3, resul);

            Console.ReadLine();

        }

        /// <summary>
        /// 求多个整数的乘积
        /// </summary>
        /// <param name="result">多个整数的乘积</param>
        /// <param name="numbers">需要求乘积的整数集合</param>
        public void GetMultResult(out int result, params int[] numbers)
        {//参数面前的out关键字表示该参数为引用传递，out关键字与ref关键字略有不同，
            //out关键字修饰的参数在传递时是不需要初始化的。
            result = 1;
            foreach (int n in numbers)
                result *= n;//计算多个整数乘积
        }
    }
}
