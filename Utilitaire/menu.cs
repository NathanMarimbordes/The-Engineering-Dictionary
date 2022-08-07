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
            vis form = new vis(); //déclare une nouvelle fenètre avec vis
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
            viscara form = new viscara(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre
        }

        private void btnVisCara_Click_1(object sender, EventArgs e)
        {

        }
    }
}
