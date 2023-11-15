price = int(input())
tax = price//11
supply = price-tax
print(*[supply, tax] if supply//10==tax else [-1])