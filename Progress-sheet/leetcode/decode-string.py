class Solution:
    def decodeString(self, s: str) -> str:
        def decode (l,r):
            initial=-1
            opening=0
            digit=''
            ans=''
            for i in range (l,r):
                if s[i].isdigit() and opening==0 :
                    digit+=s[i]
                elif s[i]=="[":
                    if opening==0:
                        initial=i
                    opening+=1  
                elif s[i]=="]":
                    opening-=1
                    if opening == 0 :
                       ans +=int(digit) * decode (initial+1,i)
                       digit=''
                elif opening==0:
                    ans +=s[i]
            return ans

        return decode (0,len(s))
        