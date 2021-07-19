using System;
using System.Text;
using System.Collections.Generic;

namespace ConsoleAppReversWords
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello World!");
            //string s = "abcd efg hijk";
            //string[] arrStr = s.Split(" ");
            //Char[] arr = s.ToCharArray();

            //Console.WriteLine(s.Length);
            //StringBuilder sb = new StringBuilder();

            ////foreach (var a in arr)
            ////{
            ////Console.WriteLine(a);

            ////}
            //sb.Append('a');
            //sb.Append('b');
            //sb.Append('c');
            //sb.Append('d');
            //Console.WriteLine(sb.ToString());
            //Console.WriteLine(sb.Length);
            //int leng = sb.Length-1;
            //sb.Remove(leng, 1);
            //Console.WriteLine(sb.ToString());

            ////Console.WriteLine(string.Join("", arr));
            //Console.WriteLine(string.Join(" ", arrStr));
            //Console.WriteLine(ReverseWords(s));
            //Console.WriteLine(ReverseWords2(s));
            //Console.WriteLine(3/2);
            //Console.WriteLine(4%2);
            //int n = 1, l = 1;
            //int[] ii = new int[] { 2, 3, 10 };
            //Console.WriteLine(MinCount(ii));
            Console.WriteLine(LengthOfLongestSubstring("abcabcbb"));


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


  
        public static int LengthOfLongestSubstring(string s)
        {
        HashSet<char> letter = new HashSet<char>();// 哈希集合，记录每个字符是否出现过
            int left = 0, right = 0;//初始化左右指针，指向字符串首位字符
            int length = s.Length;
            int count = 0, max = 0;//count记录每次指针移动后的子串长度
            while (right < length)
            {
                if (!letter.Contains(s[right]))//右指针字符未重复
                {
                    letter.Add(s[right]);//将该字符添加进集合
                    right++;//右指针继续右移
                    count++;
                }
                else//右指针字符重复，左指针开始右移，直到不含重复字符（即左指针移动到重复字符(左)的右边一位）
                {
                    letter.Remove(s[left]);//去除集合中当前左指针字符
                    left++;//左指针右移
                    count--;
                }
                max = Math.Max(max, count);
            }
            return max;
        }
        }

    }

