
class Plateau:
    def __init__ (self):
    
        self.board = [
            [-1, -1,  1,  1,  1, -1, -1],
            [-1, -1,  1,  1,  1, -1, -1],
            [ 1,  1,  1,  1,  1,  1,  1],
            [ 1,  1,  1,  0,  1,  1,  1],
            [ 1,  1,  1,  1,  1,  1,  1],
            [-1, -1,  1,  1,  1, -1, -1],
            [-1, -1,  1,  1,  1, -1, -1]
        ]
        self.historique = []  # Stocke les mouvements effectués
        
    def afficher_plateau(self):
        for row in self.board:
            ligne_affichee = ""
            for case in row:
                if case == -1:  # Case inutilisable
                    ligne_affichee += "   "  
                elif case == 0:  # Case vide
                    ligne_affichee += " . "  
                elif case == 1:  # Case avec un pion
                    ligne_affichee += " O "  # Cercle pour un pion
            print(ligne_affichee)  # Afficher la ligne
                            
    
    def movements_possible(self):
        moves = [] #une liste vide pour stocker le movements possibles 
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 1:  # Si la case est occupée
                    # Vérifiez chaque direction
                    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        mx, my = x + dx // 2, y + dy // 2
                        if (0 <= nx < len(self.board) and 0 <= ny < len(self.board[0]) and
                                self.board[nx][ny] == 0 and self.board[mx][my] == 1):
                            moves.append(((x, y), (nx, ny)))
        return moves
    
    def effectuer_deplacement(self, mouvements, indice):
     # Vérifie que l'indice est valide
        if 0 <= indice < len(mouvements):
            (x1, y1), (x2, y2) = mouvements[indice]
        
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2

            # Enregistre le mouvement dans l'historique 
            self.historique.append(((x1, y1), (x2, y2)))

            self.board[x1][y1] = 0  
            self.board[mx][my] = 0  
            self.board[x2][y2] = 1  
        else:
            print("Indice invalide : Aucun déplacement effectué.")

    def annuler_deplacement(self):
        if not self.historique:
            print("Aucun mouvement à annuler.")
            return

        # Récupérer le dernier mouvement
        (x1, y1), (x2, y2) = self.historique.pop()

        # Coordonnées de la case sautée
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2

        # Annuler le mouvement sur le plateau
        self.board[x1][y1] = 1  
        self.board[mx][my] = 1  
        self.board[x2][y2] = 0  

    #Verifie si le jeu est résolu
    def est_solved(self):
        
        # Compter le nombre total de billes sur le plateau
        compteur = sum(row.count(1) for row in self.board)
        if compteur != 1:
            return False

        # Vérifier si la dernière bille est dans la case centrale
        return self.board[3][3] == 1

    #Resolution du jeu en s'appuiyant sur le Backtracking
    def resoudre(self):
        if self.est_solved():
            return True  # Plateau résolu si la dernière bille est dans la case centrale.

        mouvements = self.movements_possible()
        if not mouvements:
            return False  # Si aucun mouvement n'est possible, échec.

        for (x1, y1), (x2, y2) in mouvements:
            # Appliquer le mouvement
            self.effectuer_deplacement(mouvements, mouvements.index(((x1, y1), (x2, y2))))

            # Appel récursif pour continuer la résolution
            if self.resoudre():
                return True  # Solution trouvée.

            # Annuler le mouvement si cela ne mène pas à une solution
            self.annuler_deplacement()

        return False  # Aucun mouvement ne mène à une solution
