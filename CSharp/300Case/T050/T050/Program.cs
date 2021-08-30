using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T050
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "修改错误的古诗----Remove方法";
            Console.WriteLine("《暮江吟》");
            string poetryRight = "一道残阳铺水中，半江瑟瑟半江红。可怜九月初三夜，露似珍珠月似弓。";
            string poetryWrong = "一道阳光铺水中，半江瑟瑟半江红。可怜九月初三夜晚，露像珍珠月像弓。";

            do
            {
                Console.WriteLine(poetryWrong);//输出错误的古诗
                Console.WriteLine("请输入功能：删除，替换");

                string function = Console.ReadLine();

                switch (function)
                {
                    case "删除":
                        Console.Write("请输入删除的字符串起始位置：");
                        int start = int.Parse(Console.ReadLine());
                        Console.Write("请输入删除的字符串长度：");
                        int lenght = int.Parse(Console.ReadLine());
                        poetryWrong = poetryWrong.Remove(start, lenght);//移动古诗中指定的字符
                        break;
                    case "替换":
                        Console.Write("请输入需要替换的字符串：");
                        string oldValue = Console.ReadLine();

                        Console.Write("请输入替换后的字符串：");
                        string newValue = Console.ReadLine();
                        poetryWrong = poetryWrong.Replace(oldValue, newValue);
                        break;
                }

            } while (poetryRight != poetryWrong);
            Console.WriteLine(poetryRight);
            Console.WriteLine("修改成功！");
            Console.ReadLine();
        }
    }
}
