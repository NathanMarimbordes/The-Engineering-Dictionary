using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Utilitaire
{
    public partial class menu : Form
    {
        public menu()
        {
            InitializeComponent();
        }

        private void vis_Click(object sender, EventArgs e)
        {
            FrmDimM_Tran_Vis_Main_Qte form = new FrmDimM_Tran_Vis_Main_Qte(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre

        }

        private void btnClavette_Click(object sender, EventArgs e)
        {
            Clavette form = new Clavette(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre
        }

        private void btnVisCara_Click(object sender,
            EventArgs e)
        {
            FrmDimM_Tran_Vis_Main_Cara form = new FrmDimM_Tran_Vis_Main_Cara(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre
        }

        private void btnVisCara_Click_1(object sender, EventArgs e)
        {

        }

        private void showSubMenu(Panel subMenu)
        {
            if(subMenu.Visible == false)
            {
                HideSubMenu();
                subMenu.Visible = true;
            }
            else
            {
                subMenu.Visible = false;
            }
        }

        private void HidePanel()
        {
            /*Ici on initialise tout les panels que l'on veux cacher*/
            pnlDimM.Visible = false;
            pnlDimM_Crea.Visible = false;
            pnlDimM_Guid.Visible = false;
            pnlDimM_Tran.Visible = false;
            pnlMflu.Visible = false;
        }

        private void HideSubMenu()
        {
            pnlDimM_Crea.Visible = false;
            pnlDimM_Guid.Visible = false;
            pnlDimM_Tran.Visible = false;
        }

        private void menu_Load(object sender, EventArgs e)
        {
            HidePanel();
        }

        private void btnDimM_Click(object sender, EventArgs e)
        {
            showSubMenu(pnlDimM);
        }

        private void btnDimM_Acco_Click(object sender, EventArgs e)
        {

        }

        private void btnMflu_Click(object sender, EventArgs e)
        {
            showSubMenu(pnlMflu);
        }

        private void btnDimM_Guid_Click(object sender, EventArgs e)
        {
            showSubMenu(pnlDimM_Guid);
        }

        private void btnDimM_Tran_Click(object sender, EventArgs e)
        {
            showSubMenu(pnlDimM_Tran);
        }

        private void btnDimM_Crea_Click(object sender, EventArgs e)
        {
            showSubMenu(pnlDimM_Crea);
        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }

        private Form activeForm = null;
        private void openChildForm(Form childForm)
        {
            if (activeForm != null)
                activeForm.Close();
            activeForm = childForm;
            childForm.TopLevel = false;
            childForm.FormBorderStyle = FormBorderStyle.None;
            childForm.Dock = DockStyle.Fill;
            pnlChildForm.Controls.Add(childForm);
            pnlChildForm.Tag = childForm;
            childForm.BringToFront();
            childForm.Show();
        }

        private void btnDimM_Tran_Viss_Click(object sender, EventArgs e)
        {
            openChildForm(new FrmDimM_Tran_Vis_Main());
        }

        private void panelLogo_Paint(object sender, PaintEventArgs e)
        {

        }

        private void FrmDimM_Guid_Roul_Click(object sender, EventArgs e)
        {
            openChildForm(new FrmDimM_Guid_Roul_Main());
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {

        }
        private void button1_Click(object sender, EventArgs e)
        {

        }
        private void btnTest_Click(object sender, EventArgs e)
        {
            openChildForm(new FrmDimM_Test());
        }


    }
}
