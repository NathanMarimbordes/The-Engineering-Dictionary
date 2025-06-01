using System;
using System.IO;
using System.Windows.Forms;
using System.Diagnostics;

namespace Utilitaire
{
    partial class FrmDimM_Test : Form
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        /// 

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
        components.Dispose();
        }
            base.Dispose(disposing);
        }

        

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnCalculer = new System.Windows.Forms.Button();
            this.txty = new System.Windows.Forms.TextBox();
            this.button3 = new System.Windows.Forms.Button();
            this.cboType = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.txtx = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.listChoix = new System.Windows.Forms.ListBox();
            this.label2 = new System.Windows.Forms.Label();
            this.btnAjouter = new System.Windows.Forms.Button();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.SuspendLayout();
            // 
            // btnCalculer
            // 
            this.btnCalculer.Location = new System.Drawing.Point(281, 67);
            this.btnCalculer.Name = "btnCalculer";
            this.btnCalculer.Size = new System.Drawing.Size(99, 23);
            this.btnCalculer.TabIndex = 35;
            this.btnCalculer.Text = "Calculer";
            this.btnCalculer.UseVisualStyleBackColor = true;
            // 
            // txty
            // 
            this.txty.Location = new System.Drawing.Point(134, 44);
            this.txty.Name = "txty";
            this.txty.Size = new System.Drawing.Size(100, 20);
            this.txty.TabIndex = 33;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(295, 330);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(125, 23);
            this.button3.TabIndex = 31;
            this.button3.Text = "Exporter";
            this.button3.UseVisualStyleBackColor = true;
            // 
            // cboType
            // 
            this.cboType.FormattingEnabled = true;
            this.cboType.Items.AddRange(new object[] {
            "Tête H",
            "Tête CHC",
            "Tête fraisé"});
            this.cboType.Location = new System.Drawing.Point(134, 115);
            this.cboType.Name = "cboType";
            this.cboType.Size = new System.Drawing.Size(121, 21);
            this.cboType.TabIndex = 26;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(25, 47);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(12, 13);
            this.label4.TabIndex = 25;
            this.label4.Text = "y";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(25, 118);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(37, 13);
            this.label3.TabIndex = 24;
            this.label3.Text = "LISTE";
            // 
            // txtx
            // 
            this.txtx.Location = new System.Drawing.Point(134, 18);
            this.txtx.Name = "txtx";
            this.txtx.Size = new System.Drawing.Size(100, 20);
            this.txtx.TabIndex = 23;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(25, 21);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(12, 13);
            this.label1.TabIndex = 20;
            this.label1.Text = "x";
            // 
            // listChoix
            // 
            this.listChoix.FormattingEnabled = true;
            this.listChoix.Location = new System.Drawing.Point(28, 204);
            this.listChoix.Name = "listChoix";
            this.listChoix.Size = new System.Drawing.Size(211, 69);
            this.listChoix.TabIndex = 21;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(25, 174);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(105, 13);
            this.label2.TabIndex = 22;
            this.label2.Text = "Choix de vis possible";
            // 
            // btnAjouter
            // 
            this.btnAjouter.Location = new System.Drawing.Point(23, 275);
            this.btnAjouter.Name = "btnAjouter";
            this.btnAjouter.Size = new System.Drawing.Size(211, 23);
            this.btnAjouter.TabIndex = 29;
            this.btnAjouter.Text = "Ajouter";
            this.btnAjouter.UseVisualStyleBackColor = true;
            // 
            // statusStrip1
            // 
            this.statusStrip1.Location = new System.Drawing.Point(0, 819);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(800, 22);
            this.statusStrip1.TabIndex = 36;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // FrmDimM_Test
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 841);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.btnCalculer);
            this.Controls.Add(this.txty);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.btnAjouter);
            this.Controls.Add(this.cboType);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtx);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.listChoix);
            this.Controls.Add(this.label1);
            this.Name = "FrmDimM_Test";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Button btnCalculer;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.ComboBox cboType;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ListBox listChoix;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnAjouter;
        private System.Windows.Forms.StatusStrip statusStrip1;
        public System.Windows.Forms.TextBox txty;
        public System.Windows.Forms.TextBox txtx;
    }
}