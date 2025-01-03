from board import Plateau

def main():
    plateau = Plateau()
    print("Plateau initial :")
    plateau.afficher_plateau()

    while True:
        # Obtenir les mouvements possibles
        moves = plateau.movements_possible()
        if not moves:
            print("Aucun mouvement possible. Fin de la simulation.")
            break

        print("\nMouvements possibles (index : mouvement) :")
        for i, ((x1, y1), (x2, y2)) in enumerate(moves):
            print(f"{i} : ({x1}, {y1}) -> ({x2}, {y2})")

        # Demander à l'utilisateur de choisir un mouvement
        choix = input("Choisissez un mouvement (index), 'a' pour annuler ou 'q' pour quitter : ")
        if choix.lower() == 'q':
            print("Simulation terminée par l'utilisateur.")
            break
        elif choix.lower() == 'a':
            plateau.annuler_deplacement()
            print("\nPlateau après annulation :")
            plateau.afficher_plateau()
            continue

        # Vérifier si l'entrée est valide
        try:
            choix = int(choix)
            if 0 <= choix < len(moves):
                plateau.effectuer_deplacement(moves, choix)
                print("\nPlateau après le mouvement :")
                plateau.afficher_plateau()
            else:
                print("Index invalide. Réessayez.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre, 'a' ou 'q'.")

if __name__ == "__main__":
    main()




