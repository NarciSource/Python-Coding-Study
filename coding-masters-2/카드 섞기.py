import sys
N,K = map(int,sys.stdin.readline().split())
A_ = [None]+list(map(int,sys.stdin.readline().split()))
from collections import defaultdict
sequences = defaultdict(list)
seq_num = 0
groups = [None]*(N+1)
assigned = [None]*(N+1)
for x in range(1,N+1):
    if not groups[x]:
        sequence = [x]
        for idx, i in enumerate(sequence):
            groups[i] = (seq_num, idx)
            if sequence[0] != A_[i]:
                sequence.append(A_[i])
        sequences[seq_num] = sequence
        seq_num += 1

    group, idx = groups[x]
    len_seq = len(sequences[group])
    moved = idx + K%len_seq
    y = sequences[group][moved%len_seq]
    assigned[y]=x

print(*assigned[1:])