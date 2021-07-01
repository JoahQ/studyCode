using System.Windows.Forms;

namespace validatePhone
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        /// <summary>
        /// 验证电话号码格式是否正确
        /// </summary>
        /// <param name="str_telephone">电话号码信息</param>
        /// <returns>方法返回布尔值</returns>
        public bool IsTelephone(string str_telephone)
        {
            return System.Text.RegularExpressions.Regex.IsMatch(str_telephone, @"^(\d{3,4}-)?\d{6,8}$");
        }

        private void Button1_Click(object sender, System.EventArgs e)
        {
            if (!IsTelephone(textBox1.Text))
            { MessageBox.Show("电话号码格式不正确！"); }
            else
            { MessageBox.Show("电话号码格式正确！"); }
        }


        public bool IsPassword(string str_password)
        {
            return
              System.Text.RegularExpressions.Regex.IsMatch
                (str_password, @"[A-Za-z]+[0-9]");
        }

        private void VPButton_Click(object sender, System.EventArgs e)
        {
            if (!IsPassword(textBox2.Text.Trim()))
            {
                MessageBox.Show("密码格式不正确！");
            }
            else
            {
                MessageBox.Show("密码格式正确！");
            }
        }
    }
}
