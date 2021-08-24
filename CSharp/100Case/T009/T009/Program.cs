using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T009
{
    class Program
    {
        class Circle
        {
            const double PI = 3.1415926f;
            public readonly int Radius = 1;

            public Circle(int radius)
            {
                Radius = radius;
            }//构造函数

            public double Area()
            {
                return PI * Radius * Radius;
            }//计算圆形面积
        }
        static void Main(string[] args)
        {
            Circle circle = new Circle(10);
            //创建一个半径为10的圆形实例
            Console.WriteLine("半径为{0}的圆形面积为{1}", circle.Radius,circle.Area());

            Console.ReadLine();
        }
    }
}
