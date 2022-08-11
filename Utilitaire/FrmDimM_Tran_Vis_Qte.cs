using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
//using ExcelTDMLib;
using Excel = Microsoft.Office.Interop.Excel;
using IronPython.Hosting;
using IronPython.Runtime;

namespace Utilitaire
{

    public partial class FrmDimM_Tran_Vis_Qte : Form
    {
        public void tri()
        {

        }


        public void stocker(string myPath, int a)
        {


        }

        private static void button3_Click(object sender, EventArgs e)
        {
        }

        private static void Main(string[] args)
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
        public void listChoix_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}

