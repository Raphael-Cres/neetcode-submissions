class Solution:
    def calPoints(self, operations: List[str]) -> int:
  
        out = []
        for i in operations:
            if i == '+':
                print("in addition")
                out.append(out[-1]+out[-2])
            elif i == 'D':
                out.append(out[-1]*2)
            elif i == 'C':
                out.pop()

            else:
                print(i)
                out.append(int(i))

            print(out)

        return sum(out)