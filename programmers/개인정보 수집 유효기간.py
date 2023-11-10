def solution(today, terms, privacies):
    to_date = lambda d: (lambda year, month, day: (year-2000)*28*12 + month*28 + day)(*map(int,d.split('.')))
    terms = {condition: int(valid) for condition, valid in [term.split() for term in terms]}
    return [i+1 for i, (date, condition) in enumerate([privaciy.split() for privaciy in privacies])
                if terms[condition]*28 <= to_date(today) - to_date(date)]

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))