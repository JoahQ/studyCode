using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T031
{
    class Program
    {
        static void Main(string[] args)
        {
            //创建并初始化数组
            string[] students = new string[6] { "张三", "李四", "王五", "赵六", "孙七", "周八" };
            //遍历一维数组
            for (int i = 0; i < students.Length; i++)
            {
                Console.Write(students[i] + "\t");
            }

            Console.WriteLine("\n将 {0} 改名为 {1}", "周八", "吴九");
            students[5] = "吴九";//为数组元素赋值
            foreach (string name in students)
                Console.Write(name + "\t");//重新遍历数组

            Console.Read();

        }
    }
}
