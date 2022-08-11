using System;

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
            this.SuspendLayout();
            // 
            // FrmDimM_Tran_Vis_Qte
            // 
            this.ClientSize = new System.Drawing.Size(1143, 560);
            this.Name = "FrmDimM_Tran_Vis_Qte";
            this.Load += new System.EventHandler(this.FrmDimM_Tran_Vis_Qte_Load);
            this.ResumeLayout(false);

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