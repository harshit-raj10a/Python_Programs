Max continuous series of 1s
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.

Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Example:

Input :
Array = [1 1 0 1 1 0 0 1 1 1]
M = 1

Output :
[0, 1, 2, 3, 4]

If there are multiple possible solutions, return the sequence which has the minimum start index.


CODE
class Solution:
    def maxone(self, A, B):
        zero=0
        zeroestot=0
        i1=0
        j1=0
        i=0
        j=0
        mini=0
        jndi=[]
        ans=[]
        while i<len(A) and j<len(A):
            if A[j]==1:
                j+=1
            elif A[j]==0:
                
                zeroestot+=1
                zero+=1
                if zero>B:
                    i=jndi.pop(0)+1
                    zero-=2
                else:
                    jndi.append(j)
                    j+=1
            ind=abs(j-i)
            if mini<ind:
                mini=ind
                i1=i
                j1=j
        if zeroestot<=B:
            i1=0
            j1=len(A)
        elif zeroestot==len(A):
            i1=0
            j1=B
        for x in range(i1,j1):
            ans.append(x)
        return ans
                
                
            
        
