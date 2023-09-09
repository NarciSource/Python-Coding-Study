import sys
def isPretty(n):
    l=len(n)
    for i in range(l):
        for j in range(i+1,l):
            if int(n)%int(n[i:j])==0 or\
                int(n)%int(n[j:])==0:
                return "YES"
    else: return "NO"    
print(isPretty(sys.stdin.readline().rstrip()))