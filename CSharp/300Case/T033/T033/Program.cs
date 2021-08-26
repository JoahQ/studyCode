using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T033
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] students = new string[] { "张三", "李四", "王五", "赵六" };
            //学生名字列表
            byte[,] results = new byte[4, 3]
            {{32,43,65},
             {62,52,62},
             {54,27,87},
             {86,95,24}};

            for (int id = 0; id < 4; id++)
            {
                int total = 0;
                for (int i = 0; i < 3; i++)
                {
                    total += results[id, i];
                }
                Console.WriteLine("{0}的总成绩为{1}", students[id], total);
            }

            Console.ReadLine();
        }
    }
}
