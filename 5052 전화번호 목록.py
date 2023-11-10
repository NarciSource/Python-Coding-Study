import sys
for t in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    call_numbers = sorted([sys.stdin.readline().strip() for _ in range(n)]) # 문자열들을 sorting하면 사전 순으로 나열됩니다.
                                                                            # 어떤 문자열의 접두사가 되는 문자열은 사전에서 바로 근접해있습니다.
    for pivot, target in zip(call_numbers, call_numbers[1:]):               # 인접한 것끼리 확인
        if target.startswith(pivot):                                        # 이 함수는 접두사인지 확인해줍니다.
            print("NO")                                                     # 길이가 작은 문자열 기준으로 판단합니다.
            break                                                           # https://github.com/python/cpython/blob/cc18b886a51672c59622837a2b8e83bf6be28c58/PC/launcher2.c#L282
    else: print("YES")