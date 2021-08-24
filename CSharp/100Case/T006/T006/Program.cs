using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T006
{
    class Program
    {
        static void Main(string[] args)
        {
            Rectangle rect = new Rectangle();
            rect.Width = 100;
            rect.Height = 1000;

            Console.WriteLine("矩形宽:{0}  矩形高:{1}", rect.Width, rect.Height);
            bool isSquare = rect.IsSquare();
            Console.WriteLine("矩形是否为正方形:{0}", isSquare);
            Console.ReadLine();
        }
    }

    struct Rectangle
    {
        public int Width;//矩形宽度
        public int Height;//矩形高度

        public bool IsSquare() {
            return Width == Height;
        }
    }
}
