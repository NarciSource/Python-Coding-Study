def solution(players, callings):

    orders = dict([(v, i) for i, v in enumerate(players)])

    for calling in callings:
        players[orders[calling]-1], players[orders[calling]] = players[orders[calling]], players[orders[calling]-1]
        orders[players[orders[calling]]] += 1
        orders[calling] -= 1

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))