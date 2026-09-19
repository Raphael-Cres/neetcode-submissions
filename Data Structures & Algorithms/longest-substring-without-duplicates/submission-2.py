class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        n = len(s)
        left = 0
        maxi = 0
        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left +=1
                print("In Boucle while")
                print(char_set)

            char_set.add(s[right])
            print("New char set")
            print(char_set)  
            maxi = max(maxi, right-left +1)
            print("Max")
            print(maxi)

        return maxi
            
        