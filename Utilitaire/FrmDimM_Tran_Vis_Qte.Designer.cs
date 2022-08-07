namespace Utilitaire
{
    partial class FrmDimM_Tran_Vis_Qte
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
            this.label1 = new System.Windows.Forms.Label();
            this.listChoix = new System.Windows.Forms.ListBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtEp = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.cboType = new System.Windows.Forms.ComboBox();
            this.listFin = new System.Windows.Forms.ListBox();
            this.label5 = new System.Windows.Forms.Label();
            this.btnAjouter = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.txtDia = new System.Windows.Forms.TextBox();
            this.txtQua = new System.Windows.Forms.TextBox();
            this.btnActualiser = new System.Windows.Forms.Button();
            this.listQua = new System.Windows.Forms.ListBox();
            this.txtQuaA = new System.Windows.Forms.TextBox();
            this.btnMoin = new System.Windows.Forms.Button();
            this.btnPlus = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(27, 62);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(103, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Epaisseur de plaque";
            // 
            // listChoix
            // 
            this.listChoix.FormattingEnabled = true;
            this.listChoix.Location = new System.Drawing.Point(438, 62);
            this.listChoix.Name = "listChoix";
            this.listChoix.Size = new System.Drawing.Size(211, 134);
            this.listChoix.TabIndex = 1;
            this.listChoix.SelectedIndexChanged += new System.EventHandler(this.listChoix_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(435, 36);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(105, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "Choix de vis possible";
            // 
            // txtEp
            // 
            this.txtEp.Location = new System.Drawing.Point(136, 59);
            this.txtEp.Name = "txtEp";
            this.txtEp.Size = new System.Drawing.Size(100, 20);
            this.txtEp.TabIndex = 3;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(27, 159);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(63, 13);
            this.label3.TabIndex = 4;
            this.label3.Text = "Type de Vis";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(27, 113);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(81, 13);
            this.label4.TabIndex = 5;
            this.label4.Text = "Diamètre de Vis";
            // 
            // cboType
            // 
            this.cboType.FormattingEnabled = true;
            this.cboType.Items.AddRange(new object[] {
            "Tête H",
            "Tête CHC",
            "Tête fraisé"});
            this.cboType.Location = new System.Drawing.Point(136, 156);
            this.cboType.Name = "cboType";
            this.cboType.Size = new System.Drawing.Size(121, 21);
            this.cboType.TabIndex = 6;
            // 
            // listFin
            // 
            this.listFin.FormattingEnabled = true;
            this.listFin.Location = new System.Drawing.Point(53, 284);
            this.listFin.Name = "listFin";
            this.listFin.Size = new System.Drawing.Size(211, 134);
            this.listFin.TabIndex = 7;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(50, 259);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(114, 13);
            this.label5.TabIndex = 8;
            this.label5.Text = "Liste de vis necessaire";
            // 
            // btnAjouter
            // 
            this.btnAjouter.Location = new System.Drawing.Point(438, 203);
            this.btnAjouter.Name = "btnAjouter";
            this.btnAjouter.Size = new System.Drawing.Size(211, 23);
            this.btnAjouter.TabIndex = 9;
            this.btnAjouter.Text = "Ajouter";
            this.btnAjouter.UseVisualStyleBackColor = true;
            this.btnAjouter.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(328, 313);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(150, 23);
            this.button2.TabIndex = 10;
            this.button2.Text = "Suprimer";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(663, 415);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(125, 23);
            this.button3.TabIndex = 11;
            this.button3.Text = "Exporter";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(27, 203);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(47, 13);
            this.label6.TabIndex = 12;
            this.label6.Text = "Quantité";
            // 
            // txtDia
            // 
            this.txtDia.Location = new System.Drawing.Point(136, 110);
            this.txtDia.Name = "txtDia";
            this.txtDia.Size = new System.Drawing.Size(100, 20);
            this.txtDia.TabIndex = 13;
            // 
            // txtQua
            // 
            this.txtQua.Location = new System.Drawing.Point(136, 200);
            this.txtQua.Name = "txtQua";
            this.txtQua.Size = new System.Drawing.Size(100, 20);
            this.txtQua.TabIndex = 14;
            // 
            // btnActualiser
            // 
            this.btnActualiser.Location = new System.Drawing.Point(284, 200);
            this.btnActualiser.Name = "btnActualiser";
            this.btnActualiser.Size = new System.Drawing.Size(99, 23);
            this.btnActualiser.TabIndex = 15;
            this.btnActualiser.Text = "Actualiser";
            this.btnActualiser.UseVisualStyleBackColor = true;
            this.btnActualiser.Click += new System.EventHandler(this.btnActualiser_Click);
            // 
            // listQua
            // 
            this.listQua.FormattingEnabled = true;
            this.listQua.Location = new System.Drawing.Point(261, 284);
            this.listQua.Name = "listQua";
            this.listQua.Size = new System.Drawing.Size(46, 134);
            this.listQua.TabIndex = 16;
            // 
            // txtQuaA
            // 
            this.txtQuaA.Location = new System.Drawing.Point(366, 284);
            this.txtQuaA.Name = "txtQuaA";
            this.txtQuaA.Size = new System.Drawing.Size(74, 20);
            this.txtQuaA.TabIndex = 17;
            // 
            // btnMoin
            // 
            this.btnMoin.Location = new System.Drawing.Point(328, 284);
            this.btnMoin.Name = "btnMoin";
            this.btnMoin.Size = new System.Drawing.Size(32, 23);
            this.btnMoin.TabIndex = 18;
            this.btnMoin.Text = "-";
            this.btnMoin.UseVisualStyleBackColor = true;
            // 
            // btnPlus
            // 
            this.btnPlus.Location = new System.Drawing.Point(446, 284);
            this.btnPlus.Name = "btnPlus";
            this.btnPlus.Size = new System.Drawing.Size(32, 23);
            this.btnPlus.TabIndex = 19;
            this.btnPlus.Text = "+";
            this.btnPlus.UseVisualStyleBackColor = true;
            // 
            // FrmDimM_Tran_Vis_Qte
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(879, 495);
            this.Controls.Add(this.btnPlus);
            this.Controls.Add(this.btnMoin);
            this.Controls.Add(this.txtQuaA);
            this.Controls.Add(this.listQua);
            this.Controls.Add(this.btnActualiser);
            this.Controls.Add(this.txtQua);
            this.Controls.Add(this.txtDia);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.btnAjouter);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.listFin);
            this.Controls.Add(this.cboType);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtEp);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.listChoix);
            this.Controls.Add(this.label1);
            this.Name = "FrmDimM_Tran_Vis_Qte";
            this.Text = " ";
            this.Load += new System.EventHandler(this.vis_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ListBox listChoix;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtEp;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ComboBox cboType;
        private System.Windows.Forms.ListBox listFin;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button btnAjouter;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox txtDia;
        private System.Windows.Forms.TextBox txtQua;
        private System.Windows.Forms.Button btnActualiser;
        private System.Windows.Forms.ListBox listQua;
        private System.Windows.Forms.TextBox txtQuaA;
        private System.Windows.Forms.Button btnMoin;
        private System.Windows.Forms.Button btnPlus;
    }
}