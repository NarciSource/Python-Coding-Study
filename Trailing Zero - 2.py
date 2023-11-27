n = int(input())

def factors(number):
    while number>0:
        number//=5
        yield number

for number in range(5,5000,5):
    if n <= sum(factors(number)):
        print(number)
        break