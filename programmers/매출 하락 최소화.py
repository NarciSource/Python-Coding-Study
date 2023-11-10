def calSales(sales, tree):
    def salesCase(leader):
        subleaders = filter(lambda e: tree[e], tree[leader])
        normals = filter(lambda e: not tree[e], tree[leader])

        subtree_sales_bundle = [salesCase(subleader) for subleader in subleaders]

        from math import inf
        subtree_minimum = sum([min((subleader_sales, subleader_absent_sales), default=inf) for subleader_sales, subleader_absent_sales in subtree_sales_bundle])
        #
        leader_sales = sales[leader] + subtree_minimum
        #
        if any([subleader_sales < subleader_absent_sales for subleader_sales, subleader_absent_sales in subtree_sales_bundle]):
            leader_absent_sales = subtree_minimum
        else:
            leader_absent_sales_case1 = min([sales[n] for n in normals], default=inf) 
            leader_absent_sales_case2 = min([subleader_sales - subleader_absent_sales for subleader_sales, subleader_absent_sales in subtree_sales_bundle], default=inf)
            leader_absent_sales = min(leader_absent_sales_case1, leader_absent_sales_case2) + subtree_minimum

        return leader_sales, leader_absent_sales
    
    return min(salesCase(leader=1)) #ceo

def links2tree(links):
    from collections import defaultdict 
    tree = defaultdict(list)
    for [a, b] in links:
        tree[a].append(b)
    return tree

def solution(sales, links):
    sales.insert(0, 0) #bound

    return calSales(sales, links2tree(links))


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
print(solution([5, 6, 5, 3, 4], [[2,3], [1,4], [2,5], [1,2]]))
print(solution([5, 6, 5, 1, 4], [[2,3], [1,4], [2,5], [1,2]]))
print(solution([10, 10, 1, 1], [[3,2], [4,3], [1,4]]))