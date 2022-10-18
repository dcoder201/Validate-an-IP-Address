#User function Template for python3

def isValid(s):
    #code here
    ans = list(s.split("."))
    if(len(ans) != 4):
        return False
    for i in s:
        if not(i.isnumeric()) or (i == "" or len(i)!= len(str(int(i))) or int(i) > 255):
            return False
    return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends
