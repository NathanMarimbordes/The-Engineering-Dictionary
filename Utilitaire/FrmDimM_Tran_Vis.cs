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
    public partial class FrmDimM_Tran_Vis : Form
    {
        public FrmDimM_Tran_Vis()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }


        private void btnQte_Click(object sender, EventArgs e)
        {
            FrmDimM_Tran_Vis_Qte form = new FrmDimM_Tran_Vis_Qte(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre

        }

        private void btnCara_Click(object sender, EventArgs e)
        {
            FrmDimM_Tran_Vis_Cara form = new FrmDimM_Tran_Vis_Cara(); //déclare une nouvelle fenètre avec vis
            form.Show(); // ouvre cette fenêtre
            Calcul form = new calcul();
        }

        private void FrmDimM_Tran_Vis_Load(object sender, EventArgs e)
        {

        }

        
    }

    void calcul()
    {
        static void Main(string[] args)
        {
            //instance of python engine
            var engine = Python.CreateEngine();
            //reading code from file
            var source = engine.CreateScriptSourceFromFile(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "PythonSampleIronPython.py"));
            var scope = engine.CreateScope();
            //executing script in scope
            source.Execute(scope);
            var classCalculator = scope.GetVariable("calculator");
            //initializing class
            var calculatorInstance = engine.Operations.CreateInstance(classCalculator);
            Console.WriteLine("From Iron Python");
            Console.WriteLine("5 + 10 = {0}", calculatorInstance.add(5, 10));
            Console.WriteLine("5++ = {0}", calculatorInstance.increment(5));
        }

    }
}
