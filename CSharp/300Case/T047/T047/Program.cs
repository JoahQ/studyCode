﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T047
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "将日期按指定格式输出----格式化日期";

            DateTime DT = DateTime.Now;
            Console.WriteLine("当前日期为：{0:d}", DT);
            Console.WriteLine("当前日期为：{0:D}", DT);

            Console.WriteLine("当前时间为：{0:t}", DT);
            Console.WriteLine("当前时间为：{0:T}", DT);

            Console.WriteLine("当前日期时间为：{0:f}", DT);
            Console.WriteLine("当前日期时间为：{0:F}", DT);

            Console.WriteLine("当前日期时间为：{0:g}", DT);
            Console.WriteLine("当前日期时间为：{0:G}", DT);

            Console.WriteLine("当前月日为：{0:M}", DT);
            Console.WriteLine("当前年月为：{0:Y}", DT);

            Console.WriteLine("当前日期为：{0:yy年MM月dd日}", DT);
            Console.WriteLine("当前日期为：{0:yyyy年MMMMdd日dddd }", DT);

            Console.WriteLine("当前时间为：{0:ttHH点mm分ss秒}", DT);

            Console.ReadLine();
        }
    }
}
