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
    public partial class FrmDimM_Guid_Roul_Main : Form
    {
        public FrmDimM_Guid_Roul_Main()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            FrmDimM_Guid_Roul_Solutions form = new FrmDimM_Guid_Roul_Solutions(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void flowLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            FrmDimM_Guid_Roul_DDV form = new FrmDimM_Guid_Roul_DDV(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre
        }
    }
}
