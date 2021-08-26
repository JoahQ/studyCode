using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace T038
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "生成省市信息表-----Dictionary的使用";
            //创建省份列表
            Dictionary<string, List<string>> provinces = new Dictionary<string, List<string>>();
            List<string> HeBei = new List<string>();
            provinces.Add("河北", HeBei);
            HeBei.Add("石家庄");
            HeBei.Add("唐山");

            List<string> ShaXi = new List<string>();
            provinces.Add("山西", ShaXi);
            ShaXi.Add("太原");
            ShaXi.Add("大同");

            List<string> JiangSu = new List<string>();
            provinces.Add("江苏", JiangSu);
            JiangSu.Add("南京");
            JiangSu.Add("苏州");

            foreach (KeyValuePair<string, List<string>> province in provinces)
            {
                Console.WriteLine("{0}省：", province.Key);
                foreach (string city in province.Value)
                {
                    Console.WriteLine("\t{0}市", city);
                }
            }
            Console.ReadLine();
            Console.WriteLine("输入需要查询的省份：");
            string pro = Console.ReadLine();
            if (provinces.ContainsKey(pro))
            {
                foreach (string city in provinces[pro])
                {
                    //遍历城市信息
                    Console.WriteLine("\t{0}市", city);
                }
            }
            else
            {
                Console.WriteLine("您需要查询的省份不存在！");
            }

            Console.ReadLine();
        }
    }
}
