class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            m1 = max(stones)
            stones.remove(m1)
            m2 = max(stones)
            stones.remove(m2)

            print(f"m1 est égal à {m1} et m2 a {m2}")

            if m1 == m2:
                continue
            else :
                stones.append(m1-m2)

        return 0 if not stones else stones[0]
        