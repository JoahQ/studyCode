﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T028
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "百钱买百鸡算法";
            for (int cock = 0; cock <= 20; cock++)//公鸡的数量为0到20只
            {
                for (int chick = 0; chick <= 99; chick += 3)//小鸡的数量为0到99只，且是3的倍数
                {
                    int hen = 100 - cock - chick;//母鸡为100减去公鸡和小鸡的数量
                    if (hen < 0 || hen > 33)//母鸡数量在0到33之间
                        continue;
                    if (cock*5 + hen*3 + chick/3 == 100)
                    {
                        //总钱数刚好等于100
                        Console.WriteLine("公鸡{0}只，母鸡{1}只，小鸡{2}只",cock,hen,chick);
                    }

                }
            }
                Console.ReadLine();
        }
    }
}
