﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ClassLibrary;


namespace T002
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            MyClass myClass = new MyClass();
            myClass.HelloWorld();

        }
    }
}
