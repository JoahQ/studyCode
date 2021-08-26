using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T007
{
    class Program
    {
        static void Main(string[] args)
        {
            Animal animal = Animal.Cat;//为枚举型变量赋值
            switch (animal)
            {
                case Animal.Dog:
                    Console.WriteLine("狗");
                    break;
                case Animal.Cat:
                    Console.WriteLine("猫");
                    break;
                case Animal.Mouse:
                    Console.WriteLine("老鼠");
                    break;
                default:
                    break;
            }
            Console.ReadLine();
        }

        enum Animal : byte
        {
            Dog = 0,
            Cat = 1,
            Mouse = 2
        }
    }
}
