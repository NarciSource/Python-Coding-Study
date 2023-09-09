www,wwb,wbw,wbb,bwb,bbb = 1,0,0,2,0,0
for _ in range(int(input())-1):
    www,wwb,wbw,wbb,bwb,bbb = bbb,wbb,bwb,wwb+bbb*2,wbw,www+wbb
print(bbb)