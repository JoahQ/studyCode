using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T010
{
    class Program
    {
        class Rectangle
        {
            public int Width, Height;//声明整型变量表示矩形的宽和高
            public int TryArea()//计算矩形面积并检测数据溢出
            {
                checked
                {
                    int area = Width * Height;

                    return area;
                }
            }

            public int Area()
            {
                return Width * Height;
            }
        }
        static void Main(string[] args)
        {
            Rectangle rect = new Rectangle();

            Console.WriteLine("请输入矩形宽度：");
            rect.Width = int.Parse(Console.ReadLine());
            //从控制台输入数据给矩形的宽赋值

            Console.WriteLine("请输入矩形高度：");
            rect.Height = int.Parse(Console.ReadLine());

            Console.WriteLine("矩形面积为：\n{0}", rect.Area());

            Console.WriteLine("矩形面积为：\n{0}", rect.TryArea());

            Console.ReadLine();
        }
    }
}
