solution = lambda t, p: len([True for i in range(len(t)-len(p)+1) if t[i:i+len(p)] <= p])

print(solution("3141592","271"))
print(solution("500220839878","7"))
print(solution("10203","15"))