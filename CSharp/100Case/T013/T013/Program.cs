using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T013
{
    class Program
    {
        static void Main(string[] args)
        {
            do
            {
                Console.WriteLine("请输入一个整数：");
                int Number = int.Parse(Console.ReadLine());
                Console.WriteLine("{0}的十六进制形式为0x{1:X8}", Number, Number);
                int NumberHex = Number & 0x000000FF;//将数值与0xFF按位与运算
                Console.WriteLine("第1个字节为：0x{0:X2}", NumberHex);

                NumberHex = Number >> 8 & 0x000000FF;//将数值右移8位与0xFF按位与运算
                Console.WriteLine("第2个字节为：0x{0:X2}", NumberHex);

                NumberHex = Number >> 16 & 0x000000FF;//将数值右移16位与0xFF按位与运算
                Console.WriteLine("第3个字节为：0x{0:X2}", NumberHex);

                NumberHex = Number >> 24 & 0x000000FF;//将数值右移24位与0xFF按位与运算
                Console.WriteLine("第4个字节为：0x{0:X2}", NumberHex);

            } while (Console.ReadLine() != "q");
        }
    }
}
