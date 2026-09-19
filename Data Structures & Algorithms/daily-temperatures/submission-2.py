from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        pile = []  # Stockera uniquement des index
        
        for i in range(len(temperatures)):
            # Tant que la pile n'est pas vide ET que la temp actuelle 
            # est plus grande que la temp du dernier jour stocké dans la pile
            while pile and temperatures[i] > temperatures[pile[-1]]:
                # On sort ce jour en attente (son index)
                index_jour_froid = pile.pop()
                
                # La distance est simplement index actuel - ancien index
                results[index_jour_froid] = i - index_jour_froid
            
            # Quoi qu'il arrive, on ajoute le jour actuel à la pile
            # car on ne sait pas encore quand il fera plus chaud que LUI
            pile.append(i)
            
        return results