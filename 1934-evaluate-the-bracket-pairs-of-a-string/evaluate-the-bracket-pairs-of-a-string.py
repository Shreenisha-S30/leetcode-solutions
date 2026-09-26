class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {}
        for key, value in knowledge:
            d[key] = value
        result = ""
        i = 0

        while i<len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i +1:j]

                if key in d:
                    result += d[key]
                else:
                    result += "?"

                i=j+1
            else:
                result += s[i]
                i +=1
        return result