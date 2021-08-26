using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T035
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("请输入年份：");
            int year = int.Parse(Console.ReadLine());

            byte[][] months = new byte[12][];
            for (int month = 0; month < 12; month++)
            {
                if (month < 7)
                {
                    //一月、三月、五月、七月为大月，每月有31天
                    if (month % 2 == 0)
                    {
                        months[month] = new byte[31];
                    }
                    else if (month == 1)
                    {
                        //二月闰年为29天，否则为28天
                        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
                            months[month] = new byte[29];
                        else
                            months[month] = new byte[28];
                    }
                    else
                    {
                        //四月、六月为小月，每月30天
                        months[month] = new byte[30];
                    }
                }
                else
                {
                    if (month % 2 == 0)
                        months[month] = new byte[30];//九月、十一月，30天
                    else
                        months[month] = new byte[31];//八月、十月、十二月，31天
                }
            }


            //遍历月份
            for (int month = 0; month < 12; month++)
            {
                Console.WriteLine("{0}月", month + 1);

                //遍历日期
                for (int day = 0; day < months[month].Length; day++)
                {
                    months[month][day] = (byte)(day + 1);
                    Console.Write("{0}日",months[month][day]);
                }
                Console.WriteLine();
 
            }
            Console.ReadLine();
        }
    }
}
