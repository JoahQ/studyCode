using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T055
{
    class Program
    {
        static void Main(string[] args)
        {
            StudentList students = new StudentList(10);//创建含有10个元素的学生信息表
            Console.WriteLine("按顺序输出学生姓名：");
            for (int i = 0; i < 10; i++)
                Console.Write(students[i].Name + "\t");

            for (int i = 0; i < 5; i++)//将学生信息表前面的元素与后面的元素互换
            {
                Student temp = students[i];
                students[i] = students[9 - i];
                students[9 - i] = temp;
            }
            Console.WriteLine();
            Console.WriteLine("输出学生信息表倒置后的学生姓名：");
            for (int i = 0; i < 10; i++)
                Console.Write(students[i].Name + "\t");

            Console.ReadLine();
        }

        public struct Student
        {
            static readonly string[] LastNames = new string[] 
            {"赵","钱","孙","李","周","吴","郑","王" };

            static readonly string[] FirstNames = new string[] { "一", "二", "三", "四", "五", "六", "七", "八" };

            static readonly Random R = new Random();

            public readonly string Name;

            public readonly int Number;

            public readonly int Grade;

            public readonly int Result;

            public Student(int num)     
            {
                this.Name = LastNames[R.Next(LastNames.Length)] //随机生成姓
                    + FirstNames[R.Next(FirstNames.Length)];//随机生成名

                this.Number = num;
                this.Grade = R.Next(1, 5);
                this.Result = R.Next(101);
            }
        }

        public class StudentList
        {
            private Student[] Students;//学生信息表

            //检索学生信息表
            public Student this[int index]
            {
                get { return Students[index]; }
                set { Students[index] = value; }
            }

            public StudentList(int count)
            {
                this.Students = new Student[count];//创建学生信息表

                //为学生信息表添加学生信息表
                for (int i = 0; i < count; i++)
                {
                    this.Students[i] = new Student(20120001 + i);
                }
            }

            public int Length 
            {
                get { return Students.Length; }//顺序表长度
            }
        }
    }
}
