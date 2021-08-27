using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T042
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "System.Char类型";

            string poetry = "日照香炉生紫烟，遥看瀑布挂前川。飞流直下三千尺，疑是银河落九天。\n";

            Console.WriteLine(poetry);

            foreach (char item in poetry)
            {
                Console.Write(item);//输出古诗中的每一个和标点
                Console.Write("\t");

                if (Char.IsPunctuation(item))
                    Console.Write("\n\n");//如果字符为标点符号则换行
            }

            Console.ReadLine();
            Console.WriteLine("\a");
            Console.ReadLine();
        }
    }
}
