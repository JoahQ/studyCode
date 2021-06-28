using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Using024
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
                        using (test a = new test())//在using语句中创建test对象
            {
                            MessageBox.Show(a.GetType().ToString());
                            a.Hello();
            }//using语句块执行完成后会自动调用test对象的Dispose方法
        }
        class test : IDisposable//定义test类实现IDisposable接口
        {
            public void Dispose()//实现接口方法
            {
                MessageBox.Show(//弹出消息对话框
                    "已经执行test对象的Dispose方法","提示");
            }

            public void Hello()
            {
                MessageBox.Show("Hello");
            }
        }
        
    }
}
