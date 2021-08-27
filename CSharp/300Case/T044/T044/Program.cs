using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T044
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "将古诗颠倒输出----Reverse方法";

            Console.WriteLine("《早发白帝城》");
            string[] poetry = new string[] {"朝辞白帝彩云间","千里江陵一日还",
            "两岸猿声啼不住","轻舟已过万重山"};

            foreach (string sentence in poetry)
            {
                char[] charss = sentence.ToCharArray();//将字符串转化成字符数组
                foreach (char item in charss.Reverse())
                    Console.Write(item);//将字符串中的字符颠倒输出
                Console.WriteLine();
            }

            Console.ReadLine();
        }
    }
}
