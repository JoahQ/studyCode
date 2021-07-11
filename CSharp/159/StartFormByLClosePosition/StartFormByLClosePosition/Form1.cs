using System;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.Win32;

namespace StartFormByLClosePosition
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            //this.Width = 900;
            //this.Height = 750;
            this.FormBorderStyle = FormBorderStyle.Fixed3D;

            int DeskWidth = Screen.PrimaryScreen.WorkingArea.Width;//获取桌面宽度
            int DeskHeight = Screen.PrimaryScreen.WorkingArea.Height;//获取桌面高度
            this.Width = Convert.ToInt32(DeskWidth * 0.8);//设置窗体宽度
            this.Height = Convert.ToInt32(DeskHeight * 0.8);//设置窗体高度

            RegistryKey myReg1, myReg2;//声明注册表对象
            myReg1 = Registry.CurrentUser;//获取当前用户注册表项
            try
            {
                myReg2 = myReg1.CreateSubKey("Software\\MySoft");//在注册表项中创建子项
                this.Location = new Point(Convert.ToInt16(myReg2.GetValue("1")), Convert.ToInt16(myReg2.GetValue("2")));//设置窗体的显示位置
            }
            catch (Exception)
            {

                throw;
            }
        }

        private void MainForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            RegistryKey myReg1, myReg2;//声明注册表对象
            myReg1 = Registry.CurrentUser;//获取当前用户注册表列表项
            myReg2 = myReg1.CreateSubKey("Software\\MySoft");//在注册表中创建子项
            try
            {
                myReg2.SetValue("1", this.Location.X.ToString());//将窗体关闭位置的x坐标写入注册表
                myReg2.SetValue("2", this.Location.Y.ToString());//将窗体关闭位置的y坐标写入注册表
            }
            catch (Exception)
            {

                throw;
            }
        }
    }
}
