maximum,minimum = 1000,-1000

def fun_alphabeta(d,node,maxP,v,A,B, pruned):
    if d == 3:
        return v[node]

    if maxP:
        best = minimum
        for i in range(2):
            value = fun_alphabeta(d+1,node*2+i,False,v,A,B, pruned)
            best = max(best, value)
            A = max(A, best)
            if B <= A:
                break
        return best

    else:
        best = maximum
        for i in range(2):
            value = fun_alphabeta(d+1,node*2+i,True,v,A,B, pruned)
            best = min(best, value)
            B = min(B, best)
            if B <= A:
                break
        if best <= A:
            pruned.append(node)
        return best

src = []
x = int(input("Enter total number of leaf node: "))
for i in range(x):
    y = int(input("Enter node value: "))
    src.append(y)

d = int(input("Enter depth value: "))
node = int(input("Enter node value: "))

pruned = []
best_score = fun_alphabeta(d, node, True, src, minimum, maximum, pruned)
print("The optimal value is", best_score)
print("Pruned nodes:", pruned)
