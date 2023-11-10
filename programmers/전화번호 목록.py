def solution(phone_book):
    phone_book.sort()
    for pivot, target in zip(phone_book, phone_book[1:]):
        if target.startswith(pivot):
            return False
    else: return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))