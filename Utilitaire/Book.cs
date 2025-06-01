namespace Utilitaire
{

	public class Donnee
	{
		public string Grandeur { get; set; }

		public int Valeur { get; set; }

		public string Unité { get; set; }

		public override string ToString()
		{
			return $"{Grandeur} - {Valeur} - {Unité}";
		}

	}

}
