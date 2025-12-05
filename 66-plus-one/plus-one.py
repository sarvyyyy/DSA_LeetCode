class Solution:
    def plusOne(self, digits: List[int]):
        n=len(digits)
        flag=False
        if digits[-1] != 9:
            digits[-1]+=1
            flag= True
        else:
            for i in range(n-1,-1,-1):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    flag=True
                    break

            if flag==False:
                digits[0]=1
                digits.append(0)
        
        return digits