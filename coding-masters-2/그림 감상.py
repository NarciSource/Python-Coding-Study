paint = [list(map({'O':0,'X':1}.get, input().strip())) for _ in range(4)]
def is_4x():
    for i in range(3):
        for j in range(3):
            if paint[i][j]+paint[i][j+1]+paint[i+1][j]+paint[i+1][j+1] == 3:
                return True
    else: return False
print("yes" if is_4x() else "no")