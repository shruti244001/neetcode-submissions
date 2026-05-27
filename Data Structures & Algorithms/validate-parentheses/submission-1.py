class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={
        "}":"{", 
        ")":"(",
        "]":"["
        }
        st=[]
        for i in s:
            if i in mapping:
                if not st or st[-1]!=mapping[i]:
                    return False
                st.pop()
            else:
                st.append(i)
        return len(st)==0
             

