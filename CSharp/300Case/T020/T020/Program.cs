﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T020
{
    class Program
    {
        static void Main(string[] args)
        {
            do
            {
            Console.WriteLine("请输入一个字符串：");
            string s = Console.ReadLine();

            foreach (var c in s)
            {
                if (c >= 'a' && c <= 'z')//判断是否为小写字母
                {
                    Console.WriteLine("{0} 是小写字母", c);
                }
                else if (c >= 'A' && c <= 'Z')//判断是否为大写字母
                {
                    Console.WriteLine("{0} 是大写字母", c);
                }
                else if (c >= '0' && c <= '9')//判断是否为十进制数字
                {
                    Console.WriteLine("{0} 是十进制数字", c);
                }
                else
                {
                    Console.WriteLine("{0} 是其他字符", c);
                }
            }
            }while(Console.ReadLine() != "q");
        }
    }
}
