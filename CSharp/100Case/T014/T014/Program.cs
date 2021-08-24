using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T014
{
    class Program
    {
        static void Main(string[] args)
        {
            do
            {
                Console.WriteLine("请输入学生成绩：");
                int Result = int.Parse(Console.ReadLine());

                if (Result >= 85)
                    Console.WriteLine("学生成绩为 A");
                if (Result < 85 && Result >= 70)
                    Console.WriteLine("学生成绩为 B");
                if (Result < 70 && Result >= 60)
                    Console.WriteLine("学生成绩为 C");
                if (Result < 60)
                    Console.WriteLine("学生成绩为 D");


            } while (Console.ReadLine() != "q");
        }
    }
}
