using System;
using System.Text;

namespace ConsoleAppReversWords
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string s = "abcd efg hijk";
            string[] arrStr = s.Split(" ");
            Char[] arr = s.ToCharArray();

            Console.WriteLine(s.Length);
            StringBuilder sb = new StringBuilder();

            //foreach (var a in arr)
            //{
            //Console.WriteLine(a);

            //}
            sb.Append('a');
            sb.Append('b');
            sb.Append('c');
            sb.Append('d');
            Console.WriteLine(sb.ToString());
            Console.WriteLine(sb.Length);
            int leng = sb.Length-1;
            sb.Remove(leng, 1);
            Console.WriteLine(sb.ToString());

            //Console.WriteLine(string.Join("", arr));
            Console.WriteLine(string.Join(" ", arrStr));
            Console.WriteLine(ReverseWords(s));
            Console.WriteLine(ReverseWords2(s));
            Console.WriteLine(3/2);
            Console.WriteLine(4%2);

            int[] ii = new int[] { 2, 3, 10 };
            Console.WriteLine(MinCount(ii));

            
        }
        public static string ReverseWords(string s)
        {
            StringBuilder sb = new StringBuilder();
            string[] arrStr = s.Split(" ");
            for(int i = 0; i < arrStr.Length ;++i)
            {
                sb.Clear();
                for (int j = arrStr[i].Length - 1; j >= 0; j--)
                {
                    sb.Append(arrStr[i][j]);
                }
                arrStr[i] = sb.ToString();
            }

            return string.Join(" ", arrStr);
        }

        public static string ReverseWords2(string s)
        {
            Char[] arr = s.ToCharArray();
            Char temp;
            int i = 0;
            int j;
            while(i<arr.Length)
            {
                j = i;
                while (i<arr.Length&&arr[i] != ' ')
                {
                    i++;
                }

                for (int left = j, right = i - 1; left < right; left++, right--)
                {
                    temp = arr[left];
                    arr[left] = arr[right];
                    arr[right] = temp;
                }


                while (i < arr.Length&& arr[i] == ' ')
                {
                    i++;
                }
            }

            return string.Join("", arr);
        }

        public static int MinCount(int[] coins)
        {
            int n = coins.Length;
            int result = 0;
            for (int i = 0; i < n; i++)
            {
                result += coins[i] / 2;
                result += coins[i] % 2;
            }
            return result;
        }
    }
}
