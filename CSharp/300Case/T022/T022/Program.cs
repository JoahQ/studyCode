using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T022
{
    class Program
    {
        enum Week : byte
        {
            a,
            Monday,
            Tuesday,
            Wednesday,
            Thursday,
            Friday,
            Saturday,
            Sunday
        }

        static void Main(string[] args)
        {

            do
            {
                Console.WriteLine("请输入星期：");
                Week week1 = (Week)byte.Parse(Console.ReadLine());
                Console.WriteLine(week1.ToString());
                Console.WriteLine();
                switch (week1)
                {
                    case Week.Sunday:
                        Console.WriteLine("星期日特价菜：爆炒牛肉18元");
                        break;
                    case Week.Monday:
                        Console.WriteLine("星期一特价菜：啤酒鸭26元");
                        break;
                    case Week.Tuesday:
                        Console.WriteLine("星期二特价菜：红烧肉20元");
                        break;
                    case Week.Wednesday:
                        Console.WriteLine("星期三特价菜：回锅肉16元");
                        break;
                    case Week.Thursday:
                        Console.WriteLine("星期四特价菜：水煮鱼24元");
                        break;
                    case Week.Friday:
                        Console.WriteLine("星期五特价菜：剁椒鱼头30元");
                        break;
                    case Week.Saturday:
                        Console.WriteLine("星期六特价菜：手撕包菜12元");
                        break;
                    default:
                        break;
                }
            } while (Console.ReadLine() != "q");
            
        }
    }
}
