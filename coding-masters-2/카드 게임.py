import sys
n = int(sys.stdin.readline())
cards = [0]*4 + list(map(int,sys.stdin.readline().split()))

cheol = [0]*4+[0]*n
young = [0]*4+[0]*n

for i in range(4,n+4):
    cheol[i] = max(young[i-3] + sum(cards[i-2:i+1]),
    young[i-2] + sum(cards[i-1:i+1]),
    young[i-1] + sum(cards[i:i+1]))
    young[i] = cheol[i-1] - cards[i]
    #young[i-3] = cheol[i-4] - cards[i-3]

print(young)
print(cheol)