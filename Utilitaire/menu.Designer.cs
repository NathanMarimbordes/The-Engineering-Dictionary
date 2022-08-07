namespace Utilitaire
{
    partial class menu
    {
        /// <summary>
        /// Variable nécessaire au concepteur.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Nettoyage des ressources utilisées.
        /// </summary>
        /// <param name="disposing">true si les ressources managées doivent être supprimées ; sinon, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Code généré par le Concepteur Windows Form

        /// <summary>
        /// Méthode requise pour la prise en charge du concepteur - ne modifiez pas
        /// le contenu de cette méthode avec l'éditeur de code.
        /// </summary>
        private void InitializeComponent()
        {
            this.vis = new System.Windows.Forms.Button();
            this.btnClavette = new System.Windows.Forms.Button();
            this.btnVisCara = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // vis
            // 
            this.vis.Location = new System.Drawing.Point(22, 85);
            this.vis.Name = "vis";
            this.vis.Size = new System.Drawing.Size(167, 89);
            this.vis.TabIndex = 0;
            this.vis.Text = "Programme Vis";
            this.vis.UseVisualStyleBackColor = true;
            this.vis.Click += new System.EventHandler(this.vis_Click);
            // 
            // btnClavette
            // 
            this.btnClavette.Location = new System.Drawing.Point(194, 85);
            this.btnClavette.Margin = new System.Windows.Forms.Padding(2);
            this.btnClavette.Name = "btnClavette";
            this.btnClavette.Size = new System.Drawing.Size(167, 89);
            this.btnClavette.TabIndex = 1;
            this.btnClavette.Text = "Clavette";
            this.btnClavette.UseVisualStyleBackColor = true;
            this.btnClavette.Click += new System.EventHandler(this.btnClavette_Click);
            // 
            // btnVisCara
            // 
            this.btnVisCara.Location = new System.Drawing.Point(365, 85);
            this.btnVisCara.Margin = new System.Windows.Forms.Padding(2);
            this.btnVisCara.Name = "btnVisCara";
            this.btnVisCara.Size = new System.Drawing.Size(167, 89);
            this.btnVisCara.TabIndex = 2;
            this.btnVisCara.Text = "Vis caractéristiques";
            this.btnVisCara.UseVisualStyleBackColor = true;
            this.btnVisCara.Click += new System.EventHandler(this.btnVisCara_Click_1);
            // 
            // menu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(750, 434);
            this.Controls.Add(this.btnVisCara);
            this.Controls.Add(this.btnClavette);
            this.Controls.Add(this.vis);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "menu";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button vis;
        private System.Windows.Forms.Button btnClavette;
        private System.Windows.Forms.Button btnVisCara;
    }
}

