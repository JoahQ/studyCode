using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace T052
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "验证IP地址字符串格式----Regex正则表达式";

            string pattern = @"^((2[5][0-5]|2[0-4][0-9]|1\d{2}|[1-9]?\d)\.){3}(2[5][0-5]|2[0-4][0-9]|1\d{2}|[1-9]?\d)$";

            Regex regex = new Regex(pattern);//创建正则表达对象

            Console.WriteLine("请输入IP地址：");
            while (!regex.IsMatch(Console.ReadLine()))
            {
                Console.WriteLine("IP地址格式错误！");
                Console.WriteLine("请输入IP地址：");

            }
            Console.WriteLine("IP地址格式正确！");

            Console.ReadLine();

            
        }
    }
}
