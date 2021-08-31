using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T051
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "拼接错乱的古诗句---StringBuilder的使用";

            string poetry = "岱宗夫如何？齐鲁青未了。造化钟神秀，阴阳割昏晓。荡胸生曾云，决眦入归鸟。会当凌绝顶，一览众山小。";
            Console.WriteLine("请将下列杜甫的《望岳》中的诗句拼接正确：");

            List<string> sentences = new List<string>();
            sentences.Add("一览众山小。");
            sentences.Add("决眦入归鸟。");

            sentences.Add("阴阳割昏晓。");
            sentences.Add("齐鲁青未了。");
            sentences.Add("岱宗夫如何？");
            sentences.Add("造化钟神秀，");
            sentences.Add("荡胸生曾云，");
            sentences.Add("会当凌绝顶，");

            for (int i = 0; i < sentences.Count; i++)
                Console.WriteLine("（{0}）{1}", i + 1, sentences[i]);

            StringBuilder builder = new StringBuilder();//可变字符串
            do
            {
                builder.Clear();
                Console.WriteLine("请输入正确的句子顺序：");
                string sequence =
                    Console.ReadLine();//从控制台读取诗句顺序
                foreach (var item in sequence)
                {
                    builder.Append(sentences[int.Parse(item.ToString()) - 1]);
                }

                Console.WriteLine(builder.ToString());
            } while (builder.ToString() != poetry);

            Console.WriteLine("拼接正确！");

            Console.ReadLine();


        }
    }
}
