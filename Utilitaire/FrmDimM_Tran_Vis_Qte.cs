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
            /*Cette fonction va lire les diférents valeurs rempli par l'utilisateurs afin de sortir les longueurs de vis adapter 
             puis va les stocker dans le tableaux choix*//*
            int i = 0, count = 0, b = 3, e, n = 0, afficher;
            string t = cboType.Text, r;
            // configure le stream reader qui va permettre de lire le fichier 
            FileStream readfileStream = new FileStream(myPath, FileMode.Open, FileAccess.Read);
            StreamReader StreamReader = new StreamReader(readfileStream);
            List<string> listLong = new List<string>(); // tableau dans lequel on va stocker les longueurs
            while (!StreamReader.EndOfStream)
            {
                /*Ici nous allons stocker toute les longueurs lue dans le fichier dans le tableau listLong, 
                 on trouver quelle i va permettre de savoir quelle longueur nous allons prendre en fon crion de l'épaisseur a sérer*/
                r = StreamReader.ReadLine();
                listLong.Add(r);
                count = count + 1;
                e = Int32.Parse(txtEp.Text);
                b = Int32.Parse(r);
                if (b < e) {
                    n = n + 1;
                }
            }
            // Permet de commencer avec la première longueur qui convient
            afficher = i + n;
            while (i < 10 && count != i + n) { //ici nous allons afficher 10 longueur qui conviennent ou s'arêter a la dernière longueur connu
                listChoix.Items.Add($"{t} M{a} x {listLong[afficher]}");
                i++;
                afficher = i + n;

            }
        }
        public void liste()
        {
            string myPath;
            int a;
            if (txtEp.Text != "" && txtDia.Text != "" && cboType.Text != "" && txtQua.Text != "")
            {
                /*Cette fonction va permettre de choisir en fonction des diférents diamètre de l'utilisaeurs 
                 * qu'est ce qui change spécifiquement en fonction de ce que vout l'utilisateurs*/
                if (txtDia.Text == "2") {
                    a = 2;
                    myPath = @"..\Donnees\Vis\M2.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "3") {
                    a = 3;
                    myPath = @"..\Donnees\Vis\M3.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "4") {
                    a = 4;
                    myPath = @"..\Donnees\Vis\M4.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "5") {
                    a = 5;
                    myPath = @"..\Donnees\Vis\M5.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "6") {
                    a = 6;
                    myPath = @"..\Donnees\Vis\M6.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "8") {
                    a = 8;
                    myPath = @"..\Donnees\Vis\M8.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "10") {
                    a = 10;
                    myPath = @"..\Donnees\Vis\M10.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "12") {
                    a = 12;
                    myPath = @"..\Donnees\Vis\M12.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "14") {
                    a = 14;
                    myPath = @"..\Donnees\Vis\M14.txt";
                    stocker(myPath, a);
                } else if (txtDia.Text == "16") {
                    a = 16;
                    myPath = @"..\Donnees\Vis\M16.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "18") {
                    a = 18;
                    myPath = @"..\Donnees\Vis\M18.txt";
                    stocker(myPath, a);
                }
                else if (txtDia.Text == "20") {
                    a = 20;
                    myPath = @"..\Donnees\Vis\M20.txt";
                    stocker(myPath, a);
                }
                else { MessageBox.Show(" Cette taille de vis n'est pas initialiser "); }
            } else
            {
                MessageBox.Show(" Tout les champs de ne sont pas rentrée ");
            }
        }

        public FrmDimM_Tran_Vis_Qte()
        {
            InitializeComponent();
        }

        private void btnActualiser_Click(object sender, EventArgs e)
        {
            listChoix.Items.Clear();
            liste();
            //System.Diagnostics.Process.Start("taille_vis.xlsx", @"...\Donnees\Vis\taille_vis.xlsx");
            // Exemple qui permet de lire la liste MessageBox.Show($"Nom {listLong[2]}");
        }


        private void vis_Load(object sender, EventArgs e)
        {
            cboType.Text = "Tête H";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            string[] tab = new string[listFin.Items.Count];
            string[] tabQua = new string[listQua.Items.Count];
            string ajout;
            int c, a;
            /*copie l'ensemble des items de la liste dans un tableau à partir de l'index 0
             copie aussi l'enssemble du tableau quantité*//*
            listFin.Items.CopyTo(tab, 0);
            listQua.Items.CopyTo(tabQua, 0);
            // condition qui permet de savoir si un éléments est sélectionner sur listChoix
            if (listChoix.SelectedIndex != -1) {
                ajout = listChoix.SelectedItem.ToString();
                // condition si dans la liste un éléments similaire a celui qu'on veut ajouter existe
                if (listFin.Items.Contains(ajout)) {
                    c = listFin.Items.Count;
                    /*    - Parcours toute la liste pour trouver quelle est l'éléments similaire
                          - Prend la valeurs de la quantité avec l'éléments 
                          - ajoute cette quantité au noouvelle éléments et créer en un nouveau*/
                    for (i = 0; i < c; i++) {
                        if (tab[i] == ajout) {
                            listQua.Items.RemoveAt(i);
                            listFin.Items.RemoveAt(i);
                            a = Int32.Parse(tabQua[i]) + Int32.Parse(txtQua.Text);
                            listFin.Items.Add(tab[i]);
                            listQua.Items.Add(Convert.ToString(a));
                        }
                    }
                } else {
                    /*si aucun éléments pareil ce trouve dans le tableau copie du nouvelle éléments*/
                    listFin.Items.Add(ajout);
                    listQua.Items.Add(txtQua.Text);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (listFin.SelectedIndex != -1)
            {
                // Suprime les éléments sélectionner par l'utilisateur
                listQua.Items.RemoveAt(listFin.SelectedIndex);
                listFin.Items.RemoveAt(listFin.SelectedIndex);
            }
        }

        public void button3_Click(object sender, EventArgs e)
        {
    /*
                class Program
            {
                static void Main(string[] args)
                {
                    try
                    {
                        var engine = Python.CreateEngine();
                        var source = engine.CreateScriptSourceFromFile("Avant_test.py");
                        var compiled_source = source.Compile();
                        var scope = engine.CreateScope();

                        //Command line argument example
                        //List list = new List();
                        //Variables qu'on va envoyer au programme python
                        //list.Add("txtDia");
                        //list.Add("txtQua");
                        //Python.GetSysModule(engine).SetVariable("argv", list);

                        MyClass my_class = new MyClass();
                        scope.SetVariable("my_class", my_class);
                        my_class.input = 20;

                        //FrmDimM_Tran_Vis.listFin.Items.Add(my_class.output);

                        compiled_source.Execute(scope);
                        Console.WriteLine("my_class", my_class.output);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Error" + ex.Message);
                    }

                    Console.Read();
                }
            }
        }
    */
    

      
            // Ici nous allons exportez les tableau de fin dans un excel
            // initialisialise les tableaux dans lesquels ont va stocker les données
            string[] tabFin = new string[listFin.Items.Count];
            string[] tabQua = new string[listQua.Items.Count];
            int i=0,nl=2,n;
            Excel.Application myexcelApplication = new Excel.Application();
            if (listFin.Items.Count != 0) //Test tableau rempli
            {
                if (myexcelApplication != null) //Test excel prêt a remplir ?
                {
                    //Stocke les deux tableau dans les cases d'excel grâce a la boucle while
                    listFin.Items.CopyTo(tabFin, 0);
                    listQua.Items.CopyTo(tabQua, 0);
                    Excel.Workbook myexcelWorkbook = myexcelApplication.Workbooks.Add();
                    Excel.Worksheet myexcelWorksheet = (Excel.Worksheet)myexcelWorkbook.Sheets.Add();
                    myexcelWorksheet.Cells[1, 1] = "Type de vis";
                    myexcelWorksheet.Cells[1, 2] = "Quantité";
                    while (listFin.Items.Count != i)
                    {
                        n = i + nl;
                        myexcelWorksheet.Cells[n, 1] = tabFin[i];
                        myexcelWorksheet.Cells[n, 2] = tabQua[i];
                        i++;
                    }
                    myexcelApplication.ActiveWorkbook.NewWindow();
                    myexcelWorkbook.Close();
                    myexcelApplication.Quit();
                } 

            } else {
                MessageBox.Show("Le tableau est vide");
            }
        }*

        public void listChoix_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
   }

