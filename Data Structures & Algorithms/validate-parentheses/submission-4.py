class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        brac_map = {"(":")", "[":"]", "{":"}"}

        for c in s:
            if c in ["(", "[", "{"]:
                brackets.append(c)

            if c in [")", "]", "}"] and brackets:
                if c == brac_map[brackets[-1]]:
                    brackets.pop()
                    continue
                else: 
                    return False

            if c in [")", "]", "}"] and not brackets:  
                return False 
            

        if not brackets:
            return True
        else: 
            return False
