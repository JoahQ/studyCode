using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T039
{
    class Program
    {
        //格式化代码快捷键ctr + k,ctr + d
        static void Main(string[] args)
        {
            Console.Title = "简单的列车售票系统----二维数组的应用";

            Random random = new Random();
            bool[,] seats = new bool[20, 5];//座位表状态表
            for (int c = 0; c < 20; c++)
            {
                for (int r = 0; r < 5; r++)
                {
                    seats[c, r] = random.Next(2) >= 1;//随机生成座位状态

                    Console.Write("[{0:D3}{1}]\t", c * 5 + r + 1, seats[c, r] ? " 已售" : " 空  ");
                }

                Console.WriteLine();
            }
            //Console.ReadLine();

            do
            {
                Console.WriteLine("请输入座号：");
                int number = int.Parse(Console.ReadLine());//输入座位号
                if (seats[(number - 1) / 5, (number - 1) % 5])
                {
                    Console.WriteLine("{0}号座位车票位已售出！", number);
                }
                else
                {
                    seats[(number - 1) / 5, (number - 1) % 5] = true;
                    //将座位设置成已售状态
                    Console.WriteLine("{0}号座位车票成功售出！{1}", number, seats[(number - 1) / 5, (number - 1) % 5].ToString());
                }


                for (int c = 0; c < 20; c++)
                {
                    for (int r = 0; r < 5; r++)
                    {
                        Console.Write("[{0:D3}{1}]\t", c * 5 + r + 1, seats[c, r] ? " 已售" : " 空  ");
                    }

                    Console.WriteLine();
                }
            } while (Console.ReadLine() != "q");
            //Console.ReadLine();
        }
    }
}
