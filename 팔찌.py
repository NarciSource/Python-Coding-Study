import sys
bracelet1 = sys.stdin.readline().strip()
bracelet2 = sys.stdin.readline().strip()
print("YES" if any((bracelet1*2)[i:].startswith(bracelet2) for i in range(len(bracelet1))) else "NO")