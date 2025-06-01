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
    public partial class FrmDimM_Tran_Vis_Main : Form
    {
        public FrmDimM_Tran_Vis_Main()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }
      

        private void btnQte_Click(object sender, EventArgs e)
        {
            FrmDimM_Tran_Vis_Main_Qte form = new FrmDimM_Tran_Vis_Main_Qte(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre
        }

        private void btnCara_Click(object sender, EventArgs e)
        {
            FrmDimM_Tran_Vis_Main_Cara form = new FrmDimM_Tran_Vis_Main_Cara(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre
        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}
