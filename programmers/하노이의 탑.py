def solution(n):
    answer = []
    stack = [[n, 1, 2, 3]]

    while stack:
        n, to, via, dest = stack.pop()

        if n==1:
            answer.append([to, dest])
        else:
            stack.append((n-1, via, to, dest)) #step3
            stack.append((1, to, via, dest)) #step2
            stack.append((n-1, to, dest, via)) #step1

    return answer