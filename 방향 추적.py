import sys
N = int(sys.stdin.readline())
positions = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
for (pre_a,pre_b), (cur_a,cur_b) in zip(positions[:-1], positions[1:]):
    print(1 if pre_a<cur_a else
          2 if pre_b<cur_b else
          3 if pre_a>cur_a else
          4, abs(cur_a-pre_a+cur_b-pre_b))