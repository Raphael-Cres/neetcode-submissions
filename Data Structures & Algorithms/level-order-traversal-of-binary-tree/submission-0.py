from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. La sécurité : si l'arbre est vide, on renvoie une liste vide
        if not root:
            return []
            
        resultat = []
        
        # 2. On initialise notre file d'attente avec le premier niveau (la racine)
        file = deque([root])
        
        while file:
            niveau_actuel = []
            taille_du_niveau = len(file) # Combien de nœuds sur cet étage ?
            
            # 3. On traite UNIQUEMENT les nœuds de l'étage actuel
            for _ in range(taille_du_niveau):
                # On sort le premier nœud de la file d'attente
                noeud = file.popleft()
                niveau_actuel.append(noeud.val)
                
                # On ajoute ses enfants à la fin de la file pour le PROCHAIN étage
                if noeud.left:
                    file.append(noeud.left)
                if noeud.right:
                    file.append(noeud.right)
                    
            # 4. L'étage est terminé, on l'ajoute à notre grand résultat
            resultat.append(niveau_actuel)
            
        return resultat