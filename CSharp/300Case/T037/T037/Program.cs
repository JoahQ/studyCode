using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T037
{
    class Program
    {
        struct Student
        {
            public string Name;
            public byte Age;
            public string Sex;
            public int ID;

            public Student(string name, byte age, string sex, int id)
            {
                Name = name;
                Age = age;
                Sex = sex;
                ID = id;
            }
        }
        static void Main(string[] args)
        {
            List<Student> students = new List<Student>();
            students.Add(new Student("张三", 20, "男", 20120001));
            students.Add(new Student("李四", 19, "女", 20120002));
            students.Add(new Student("王五", 18, "男", 20120003));
            students.Add(new Student("赵六", 21, "男", 20120004));

            Console.WriteLine("遍历学生信息表，输出学生信息：");
            foreach (Student s in students)
            {
                Console.WriteLine("{0}\t{1}岁\t{2}生\t{3}号", s.Name, s.Age, s.Sex, s.ID);
            }
            Console.ReadLine();

            Console.WriteLine("删除学生“李四”的信息！");
            students.RemoveAt(1);
            Console.WriteLine("在表头插入学生“孙七”的信息！");
            students.Insert(0, new Student("孙七", 22, "男", 20120005));
            Console.WriteLine("在表尾插入学生“周八”的信息！");
            students.Insert(4, new Student("周八", 17, "男", 20120006));

            Console.WriteLine("重新遍历学生信息表，输出学生信息：");
            foreach (Student s in students)
            {
                Console.WriteLine("{0}\t{1}岁\t{2}生\t{3}号", s.Name, s.Age, s.Sex, s.ID);
            }

            Console.ReadLine();
        }
    }
}
