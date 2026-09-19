class Solution:
    
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        pile = []
        for j in s:
            if j in mapping.keys():
                # On ajoute "if pile" pour s'assurer que la pile n'est pas vide avant de lire pile[-1]
                if pile and pile[-1] == mapping[j]:
                    pile.pop(-1)
                else:
                    return False
            else:
                pile.append(j)

        # À la fin, la chaîne est valide SI ET SEULEMENT SI la pile est vide
        return len(pile) == 0