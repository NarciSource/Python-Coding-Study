import sys
answer = sys.stdin.readline().rstrip()
for i in range(2,len(answer)//2+3,2):
    f,e = answer[:i],answer[i:]
    fl,el = len(f)//2,len(e)//2
    if f[:fl] == f[fl:] and e[:el] == e[el:]:
        print("YES\n"+f[:fl]+e[el:])
        break
else: print("NO")