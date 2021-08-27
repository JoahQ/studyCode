using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T041
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Stack的使用";
            do
            {
                Console.WriteLine("请输入带括号的表达式：");
                string expression = Console.ReadLine();
                if (expression == string.Empty)
                    continue;

                bool check = true;
                Stack<char> brackets = new Stack<char>();
                foreach (char bracket in expression)
                {
                    if (bracket == '(' || bracket == '[' || bracket == '{')
                    {
                        brackets.Push(bracket);//括号进入栈
                    }
                    else if ((bracket == ')' && brackets.Count == 0
                        || bracket == ']' && brackets.Count == 0
                        || bracket == '}' && brackets.Count == 0) 
                        || (bracket == ')' && brackets.Pop() != '(' 
                        || bracket == ']' && brackets.Pop() != '[' 
                        || bracket == '}' && brackets.Pop() != '{'))
                    {
                        //Console.WriteLine("表达式括号格式错误！");
                        check = false;
                        break;
                    }

                }

                if (check)
                    Console.WriteLine("表达式括号格式正确！");
                else
                    Console.WriteLine("表达式括号格式错误！");

            } while (Console.ReadLine() != "q");
        }
    }
}
