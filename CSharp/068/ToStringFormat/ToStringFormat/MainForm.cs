using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ToStringFormat
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += string.Format("{0}", DateTime.Now.ToString("F"));
            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += string.Format("{0}", DateTime.Now.ToString("f"));
            
            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += string.Format("{0}", DateTime.Now.ToString("D"));
            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += string.Format("{0}", DateTime.Now.ToString("d"));

            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += string.Format("{0}", DateTime.Now.ToString("G"));
            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += string.Format("{0}", DateTime.Now.ToString("g"));

            lb_Format.Text += Environment.NewLine;
            lb_Format.Text += string.Format("{0}", DateTime.Now.ToString("yyyy-MM-dd hh:ss:ff"));
        }
    }
}
