﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T027
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 10; i++)
            {
                for (int j = 10; j > i; j--)
                {
                    Console.Write(" ");//输出空格
                }
                
                for (int k = 0; k < i; k++)
                {
                    Console.Write("* ");//输出*
                }
                
                Console.WriteLine();//换行
 
            }
            Console.ReadLine();
        }
    }
}
