import json
with open("./Settings.json","r") as f:
    Dict = json.load(f)
    W = Dict["maxWeight"]
    print(f"W = {W}")
with open("./WeightList.txt","r") as f:
    w = f.readlines()
    w = list(map(int,[0]+w))# w[0]はダミー
    n = len(w)-1# w[0]はダミー
    print(f"w_items = {len(w)-1}")


M = [[0 for x in range(W+1)] for y in range(n+1)]

#for j in range(W+1):
#    M[0][j] = 0
for i in range(1, n+1):
    for j in range(W+1):
        if j < w[i]:
            M[i][j] = M[i-1][j]
        else:
            M[i][j] = max(M[i-1][j], w[i]+M[i-1][j-w[i]])
print(f"optimalValue {M[n][W]}")

# 最適解を求める
optimalSolution = [[["*"] for x in range(W+1)] for y in range(n+1)]
for i in range(1, n+1):
    for j in range(W+1):
        if j < w[i]:
            optimalSolution[i][j] = optimalSolution[i-1][j]
        elif M[i][j] == M[i-1][j] and M[i][j] == w[i] + M[i-1][j-w[i]]:
            optimalSolution[i][j] = optimalSolution[i-1][j] + [x+f"_{i}" for x in optimalSolution[i-1][j-w[i]]]
        elif M[i][j] == M[i-1][j]:
            optimalSolution[i][j] = optimalSolution[i-1][j]
        else:# M[i][j] == w[i] + M[i-1][j-w[i]]:
            optimalSolution[i][j] = [x+f"_{i}" for x in optimalSolution[i-1][j-w[i]]]

print(f"optimalSolution {optimalSolution[n][W]}")