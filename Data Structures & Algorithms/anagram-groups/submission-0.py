from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def is_anagram(st1, st2):
            
            def compter_lettres(st):
                d = {}
                for i in st:
                    if i not in d:
                        d[i] = 1
                    else:
                        d[i] += 1
                return d
            
          
            if len(st1) != len(st2):
                return False
                
            if compter_lettres(st1) == compter_lettres(st2):
                return True
            return False


        L = []
        
        # Nous allons "consommer" la liste strs.
        # Pour ne pas détruire l'originale, on travaille sur une copie.
        mots_a_traiter = list(strs)
        
        # Tant qu'il reste des mots à traiter...
        while mots_a_traiter:
            
            # 1. On prend le PREMIER mot de la liste et on le retire.
            #    C'est l'équivalent de votre premier "strs.remove(i)"
            mot_actuel = mots_a_traiter.pop(0)
            
            # 2. On commence le nouveau groupe avec ce mot.
            l_i = [mot_actuel]
            
            # 3. On prépare la liste pour le *prochain* tour de boucle.
            #    Cette liste contiendra les mots qui ne sont PAS
            #    des anagrammes du 'mot_actuel'.
            prochains_mots_a_traiter = []
            
            # 4. On boucle sur les mots qui restaient.
            for mot_a_tester in mots_a_traiter:
                
                # 5. On vérifie si c'est un anagramme
                if is_anagram(mot_actuel, mot_a_tester):
                    # Si oui, on l'ajoute au groupe
                    l_i.append(mot_a_tester)
                    # On NE l'ajoute PAS à 'prochains_mots_a_traiter',
                    # ce qui équivaut à votre "strs.remove(j)"
                else:
                    # Si non, il "survit" pour le prochain tour
                    prochains_mots_a_traiter.append(mot_a_tester)
            
            # 6. Le groupe est complet, on l'ajoute au résultat final.
            L.append(l_i)
            
            # 7. On met à jour la liste des mots à traiter pour le
            #    prochain tour de la boucle 'while'.
            mots_a_traiter = prochains_mots_a_traiter
            
        return L