namespace Utilitaire
{
    partial class FrmDimM_Tran_Vis_Main
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
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
            this.btnClose = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.label1 = new System.Windows.Forms.Label();
            this.btnQte = new System.Windows.Forms.Button();
            this.panel2 = new System.Windows.Forms.Panel();
            this.label2 = new System.Windows.Forms.Label();
            this.btnCara = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnClose
            // 
            this.btnClose.Location = new System.Drawing.Point(581, 422);
            this.btnClose.Name = "btnClose";
            this.btnClose.Size = new System.Drawing.Size(91, 27);
            this.btnClose.TabIndex = 2;
            this.btnClose.Text = "Fermer";
            this.btnClose.UseVisualStyleBackColor = true;
            this.btnClose.Click += new System.EventHandler(this.btnClose_Click);
            // 
            // panel1
            // 
            this.panel1.AutoSize = true;
            this.panel1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(32)))), ((int)(((byte)(39)))));
            this.panel1.Controls.Add(this.label1);
            this.panel1.Controls.Add(this.btnQte);
            this.panel1.Cursor = System.Windows.Forms.Cursors.AppStarting;
            this.panel1.Location = new System.Drawing.Point(362, 35);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(264, 162);
            this.panel1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Dock = System.Windows.Forms.DockStyle.Top;
            this.label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.label1.Location = new System.Drawing.Point(0, 0);
            this.label1.Margin = new System.Windows.Forms.Padding(20, 20, 3, 0);
            this.label1.Name = "label1";
            this.label1.Padding = new System.Windows.Forms.Padding(20, 10, 0, 0);
            this.label1.Size = new System.Drawing.Size(98, 23);
            this.label1.TabIndex = 1;
            this.label1.Text = "Quantité de vis";
            // 
            // btnQte
            // 
            this.btnQte.Location = new System.Drawing.Point(170, 132);
            this.btnQte.Name = "btnQte";
            this.btnQte.Size = new System.Drawing.Size(91, 27);
            this.btnQte.TabIndex = 0;
            this.btnQte.Text = "Ouvrir";
            this.btnQte.UseVisualStyleBackColor = true;
            this.btnQte.Click += new System.EventHandler(this.btnQte_Click);
            // 
            // panel2
            // 
            this.panel2.AutoSize = true;
            this.panel2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(32)))), ((int)(((byte)(39)))));
            this.panel2.Controls.Add(this.label2);
            this.panel2.Controls.Add(this.btnCara);
            this.panel2.Cursor = System.Windows.Forms.Cursors.AppStarting;
            this.panel2.Location = new System.Drawing.Point(49, 35);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(264, 162);
            this.panel2.TabIndex = 2;
            this.panel2.Paint += new System.Windows.Forms.PaintEventHandler(this.panel2_Paint);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Dock = System.Windows.Forms.DockStyle.Top;
            this.label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.label2.Location = new System.Drawing.Point(0, 0);
            this.label2.Margin = new System.Windows.Forms.Padding(20, 20, 3, 0);
            this.label2.Name = "label2";
            this.label2.Padding = new System.Windows.Forms.Padding(20, 10, 0, 0);
            this.label2.Size = new System.Drawing.Size(139, 23);
            this.label2.TabIndex = 1;
            this.label2.Text = "Caractéristiques des Vis";
            // 
            // btnCara
            // 
            this.btnCara.Location = new System.Drawing.Point(170, 132);
            this.btnCara.Name = "btnCara";
            this.btnCara.Size = new System.Drawing.Size(91, 27);
            this.btnCara.TabIndex = 0;
            this.btnCara.Text = "Ouvrir";
            this.btnCara.UseVisualStyleBackColor = true;
            this.btnCara.Click += new System.EventHandler(this.btnCara_Click);
            // 
            // FrmDimM_Tran_Vis_Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(684, 461);
            this.Controls.Add(this.btnClose);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "FrmDimM_Tran_Vis_Main";
            this.Text = "Form1";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnClose;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnQte;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnCara;
    }
}