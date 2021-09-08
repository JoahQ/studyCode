using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T053
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "提取古诗中含有“明月”的诗句----Contains方法";

            Console.WriteLine("《静月思》");
            string[] poetry = new string[] { "床前明月光，", "疑是地上霜。", "举头望明月，", "低头思故乡。" };

            foreach (string sentence in poetry)
                Console.WriteLine(sentence);
            Console.WriteLine("含有“明月”的诗句为：");
            foreach (string sentence in poetry)
            {
                if (sentence.Contains("明月"))
                    Console.WriteLine(sentence);
            }

            Console.ReadLine();
        }
    }
}
