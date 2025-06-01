import sys
import pandas as pd
import os

def calculer_resistance(diametre, longueur):
    # Placeholder pour la vraie formule de r�sistance
    return diametre * longueur * 0.1  # Exemple simple

def main():
    if len(sys.argv) < 2:
        print("Fichier CSV manquant")
        return

    csv_path = sys.argv[1]
    df = pd.read_csv(csv_path)

    diametre = df.iloc[0]['Diam�tre']
    longueur = df.iloc[0]['Longueur']
    resistance = calculer_resistance(diametre, longueur)

    # Choix du dossier de sortie
    print("S�lectionnez un dossier de sortie pour les r�sultats...")
    from tkinter import Tk, filedialog
    root = Tk()
    root.withdraw()
    dossier = filedialog.askdirectory(title="Choisir un dossier de sortie")
    if not dossier:
        print("Aucun dossier s�lectionn�.")
        return

    output_path = os.path.join(dossier, "resultats.csv")
    result_df = pd.DataFrame([{
        "Diam�tre": diametre,
        "Longueur": longueur,
        "R�sistance calcul�e": resistance
    }])
    result_df.to_csv(output_path, index=False)
    print(f"R�sultat enregistr� dans : {output_path}")

if __name__ == "__main__":
    main()


