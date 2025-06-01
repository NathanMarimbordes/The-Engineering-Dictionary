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
using Microsoft.Scripting.Hosting;
using CsvHelper;
using System.Globalization;
using CsvHelper.Configuration;

namespace Utilitaire
{
    public partial class FrmDimM_Test : Form
    {

    
        /*
        public void Lecture(string myPath, int a)
        {
            int x, y;
            x = Int32.Parse(txtx.Text);
            y = Int32.Parse(txty.Text);

            
        }*/

        public FrmDimM_Test()
        {
            InitializeComponent();
        }

        /*private void btnActualiser_Click(object sender, EventArgs e)
        {
            listChoix.Items.Clear();
            Lecture();
            //System.Diagnostics.Process.Start("taille_vis.xlsx", @"...\Donnees\Vis\taille_vis.xlsx");
            // Exemple qui permet de lire la liste MessageBox.Show($"Nom {listLong[2]}");
        }
        */

        private void button3_Click(object sender, EventArgs e)
        {
            int i = 3; //nbre colonnes
            string[] tabGrandeur = new string[i];
            string[] tabValeur = new string[i]; 
            string[] tabUnité = new string[i];

            // Ici nous allons exportez les tableau de fin dans un excel
            // initialisialise les tableaux dans lesquels ont va stocker les données

            int nmax = 5, nmin=2; //nbre lignes, changer nmax pour le nombre total de valeurs à copier (ne pas oublier nmax = nbre lignes 
            int n = nmin; //on assigne nmin à n

            Excel.Application myexcelApplication = new Excel.Application();
           
            if (myexcelApplication != null) //Test excel prêt a remplir ?
            {
                /*Stocke les deux tableau dans les cases d'excel grâce a la boucle while*/

                Excel.Workbook myexcelWorkbook = myexcelApplication.Workbooks.Add();
                Excel.Worksheet myexcelWorksheet = (Excel.Worksheet)myexcelWorkbook.Sheets.Add();
                myexcelWorksheet.Cells[1, 1] = "Grandeur";
                myexcelWorksheet.Cells[1, 2] = "Valeur";
                myexcelWorksheet.Cells[1, 3] = "Unité";


                while (n < nmax)
                { 
                    myexcelWorksheet.Cells[n, 1] = tabGrandeur[n];
                    myexcelWorksheet.Cells[n, 2] = tabValeur[n];
                    myexcelWorksheet.Cells[n, 3] = tabUnité[n];
                    n++;
                }
                myexcelApplication.ActiveWorkbook.NewWindow();
                myexcelWorkbook.Close();
                myexcelApplication.Quit();

            }

            
            else
            {
                MessageBox.Show("Le tableau est vide");
                //Premiere valeur : d
                //Seconde valeur : D
                //PatchParameter(10, 25);


            }
        }
        /*
        public void btnActualiser_Click(object sender, EventArgs e)
        {

            int x, y;
            x = Int32.Parse(txtx.Text);
            y = Int32.Parse(txty.Text);

            var engine = Python.CreateEngine(); // Extract Python language engine from their grasp
            var scope = engine.CreateScope(); // Introduce Python namespace (scope)
            Dictionary<string, int> valeurs = new Dictionary<string, int>()
            {
                { "x", x},
                { "y", y}
            }; // Add some sample parameters. Notice that there is no need in specifically setting the object type, interpreter will do that part for us in the script properly with high probability

            //scope.SetVariable("params", valeurs); // This will be the name of the dictionary in python script, initialized with previously created .NET Dictionary

            ScriptSource source = engine.CreateScriptSourceFromFile("0Test.py"); // Load the script
            object result = source.Execute(scope);
            var resultat = scope.GetVariable<string>("resultat"); // To get the finally set variable 'parameter' from the python script
        }*/

        private void btnCalculer_Click(object sender, EventArgs e)
        {
            double diametre, longueur;

            if (double.TryParse(txtx.Text, out diametre) &&
                double.TryParse(tyty.Text, out longueur))
            {
                string projectPath = AppDomain.CurrentDomain.BaseDirectory;
                string csvPath = Path.Combine(projectPath, "dimensions.csv");

                // Enregistre dans le fichier CSV
                File.WriteAllText(csvPath, $"Diamètre,Longueur\n{diametre},{longueur}");

                // Appelle le script Python
                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = "python",
                    Arguments = $"calcul_resistance.py \"{csvPath}\"",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true
                };

                Process process = Process.Start(psi);
                string output = process.StandardOutput.ReadToEnd();
                string error = process.StandardError.ReadToEnd();
                process.WaitForExit();

                MessageBox.Show("Script Python exécuté.\n" + output + error);
            }
            else
            {
                MessageBox.Show("Veuillez entrer des valeurs valides.");
            }
        }

        /*public void btnCalculer_Click(object sender, EventArgs e)
        {

            ///////////// ECRITURE DU CSV ///////////////
            var x = Int32.Parse(txtx.Text);
            var y = Int32.Parse(txty.Text);

            var DonneeIn = new List<Donnee>()
            {
                new Donnee {Grandeur = "x", Valeur = x, Unité = "m"},
                new Donnee {Grandeur = "y", Valeur = y, Unité = "m"},
            };

            using (var writer = new StreamWriter("Book.csv"))
            using (var csv = new CsvWriter(writer, new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                Delimiter = ";"
            }))

            csv.WriteRecords(DonneeIn);


            ///////////// EXECUTION DU PROGRAMME PYTHON ///////////////

            //var engine = Python.CreateEngine(); // Extract Python language engine from their grasp
            //dynamic scope = engine.CreateScope(); // Introduce Python namespace (scope
            //ScriptSource source = engine.CreateScriptSourceFromFile("0Test.py"); // Load the script
            //var resultat = scope.GetVariable<string>("resultat"); // To get the finally set variable 'parameter' from the python script
            
            
            ScriptEngine engine = Python.CreateEngine();
            ScriptSource script = engine.CreateScriptSourceFromFile("0Test.py");
            dynamic scope = engine.CreateScope();
            script.Execute(scope);

            
            ///////////// LECTURE DU CSV ///////////////

            using (var reader = new StreamReader("Book.csv"))
            using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
            {
                var DonneOut = csv.GetRecords<Donnee>();
                Console.WriteLine(DonneOut);
            }

            





        }
        */

        /* Début de la boucle test pour un iron Python improvisé 

        private void Main(string[] args)
        {
            //instance of python engine
            var engine = Python.CreateEngine();
            //reading code from file
            var source = engine.CreateScriptSourceFromFile(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "0Test.py"));
            var scope = engine.CreateScope(); 
            //executing script in scope
            source.Execute(scope);
            var classCalculator = scope.GetVariable("calculator");
            //initializing class
            var calculatorInstance = engine.Operations.CreateInstance(classCalculator);
            Console.WriteLine("From Iron Python");
            Console.WriteLine("On donne les valeurs de A=d*D et B=R*e : {0}", calculatorInstance.Calcul(5, 10,4,8));
        
        }

        private void listChoix_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }*/
    }


}