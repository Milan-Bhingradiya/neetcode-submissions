class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in strs:
            encoded+=str(len(i))+'#'+i
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decode=""
        i=0
        n=len(s)
        j=0

        ans=[]
        while i<n and j<n:
            j=i
            while s[j]!='#':
                j+=1
            
            num_size=int(s[i:j])
            ans.append(s[j+1:j+1+num_size])
            i=j+1+num_size
        return ans







