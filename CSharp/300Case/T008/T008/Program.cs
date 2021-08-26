using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T008
{
    class Program
    {
        struct Column
        {
            public Circle Circle;//底面圆形
            public int Height;//圆柱体高度
        }
        class Circle
        {
            public int Radius;//半径
        }
        static void Main(string[] args)
        {
            Column column1 = new Column();
            //创建圆柱体1
            Circle circle1 = new Circle();
            //创建圆形1
            column1.Height = 20;
            //设置圆柱体1的高度
            column1.Circle = circle1;
            //将圆形1赋值给圆柱体1底面圆形
            circle1.Radius = 10;
            //设置圆形1半径
            Console.WriteLine("圆柱体1高度:{0}", column1.Height);
            //输出圆柱体1的高度
            Console.WriteLine("圆柱体1底面半径：{0}", column1.Circle.Radius);
            //输出圆柱体1底面半径
            Console.WriteLine("将圆柱体1赋值给圆柱体2");

            Console.WriteLine();

            Column column2 = column1;
            Console.WriteLine("将圆形1半径改为30");
            circle1.Radius = 30;
            Console.WriteLine("圆柱体1底面半径：{0}", column1.Circle.Radius);
            Console.WriteLine("圆柱体2底面半径：{0}", column2.Circle.Radius);

            Console.WriteLine("圆柱体1高度：{0}", column1.Height);
            Console.WriteLine("圆柱体2高度：{0}", column2.Height);

            Console.WriteLine("将圆柱体2高度改为40");
            column2.Height = 40;
            Console.WriteLine("圆柱体1高度：{0}", column1.Height);
            Console.WriteLine("圆柱体2高度：{0}", column2.Height);

            Console.ReadLine();
        }
    }
}
