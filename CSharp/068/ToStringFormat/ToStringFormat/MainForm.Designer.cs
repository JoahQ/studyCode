
namespace ToStringFormat
{
    partial class MainForm
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.lb_Format = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lb_Format
            // 
            this.lb_Format.AutoSize = true;
            this.lb_Format.Location = new System.Drawing.Point(104, 41);
            this.lb_Format.Name = "lb_Format";
            this.lb_Format.Size = new System.Drawing.Size(60, 15);
            this.lb_Format.TabIndex = 0;
            this.lb_Format.Text = "格式化:";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.lb_Format);
            this.Name = "MainForm";
            this.Text = "使用ToString方法格式化日期";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_Format;
    }
}

