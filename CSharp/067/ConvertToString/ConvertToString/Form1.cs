using System;
using System.Windows.Forms;


namespace ConvertToString
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            string s = string.Format("{0}/{1}/{2}",
                textBox_Y.Text, textBox_M.Text, textBox_D.Text);
            //DateTime dt = DateTime.ParseExact(s,"yyyy/MM/dd",null);
            DateTime p_dt = DateTime.Parse(s);
            MessageBox.Show("输入的日期为：" + p_dt.ToLongDateString(),"提示！");
            //MessageBox.Show("输入的日期为：" + dt.ToLongDateString(),"提示！");
        }
    }
}
