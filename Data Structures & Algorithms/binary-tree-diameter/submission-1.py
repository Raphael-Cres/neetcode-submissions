class Solution:
    def __init__(self):
        # On crée notre variable de classe pour mémoriser le record absolu.
        # Au début, le plus grand diamètre qu'on a vu est 0.
        self.diametre_max = 0 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # On lance notre explorateur (la fonction juste en dessous)
        self.calculer_profondeur(root)
        
        # Une fois que l'explorateur a fouillé tout l'arbre, notre record
        # sera à jour. On a juste à le renvoyer.
        return self.diametre_max

    def calculer_profondeur(self, noeud):
        # 1. LA CONDITION D'ARRÊT
        # Si la boîte (le noeud) est vide, quelle est sa profondeur ?
        if noeud is None:
            return 0
        
        # 2. EXPLORATION
        # On demande la profondeur maximale du côté gauche et du côté droit.
        # (Indice : c'est ici qu'on utilise la récursivité en rappelant la fonction)
        profondeur_gauche = self.calculer_profondeur(noeud.left)
        profondeur_droite = self.calculer_profondeur(noeud.right)
        
        # 3. LE RECORD !
        # Le diamètre qui passe par ce noeud précis, c'est gauche + droite.
        # On met à jour self.diametre_max si ce résultat bat le record actuel.
        # (Indice : tu peux utiliser la fonction max(..., ...))
        self.diametre_max = max(self.diametre_max, profondeur_gauche + profondeur_droite)
        
        # 4. LE RETOUR DE LA FONCTION
        # N'oublie pas : cette fonction sert avant tout à calculer la profondeur !
        # Que doit-elle renvoyer pour que le parent sache combien d'étages il y a en dessous ?
        # (Indice : on l'a vu juste avant, c'est le max entre la gauche et la droite, + 1)
        return 1 + max(profondeur_gauche, profondeur_droite)