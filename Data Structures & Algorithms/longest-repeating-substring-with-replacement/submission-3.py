class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        compteur = {}
        max_frequence = 0
        gauche = 0
        len_max = 0
        
        for droite in range(len(s)):
            # 1. Ajouter le caractère de droite à la fenêtre
            lettre_actuelle = s[droite]
            compteur[lettre_actuelle] = compteur.get(lettre_actuelle, 0) + 1
            
            # 2. Mettre à jour la fréquence maximale historique de la fenêtre
            max_frequence = max(max_frequence, compteur[lettre_actuelle])
            
            # 3. Si la fenêtre devient invalide, on la rétrécit par la gauche
            taille_fenetre = droite - gauche + 1
            if taille_fenetre - max_frequence > k:
                lettre_gauche = s[gauche]
                compteur[lettre_gauche] -= 1
                gauche += 1
                # On ne met pas à jour taille_fenetre ici car on l'utilise pour len_max juste après
                
            # 4. Mettre à jour la longueur maximale trouvée
            # (droite - gauche + 1) représente la taille de la fenêtre actuelle
            len_max = max(len_max, droite - gauche + 1)
            
        return len_max