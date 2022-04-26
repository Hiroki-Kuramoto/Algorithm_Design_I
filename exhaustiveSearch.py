import json
with open("./Settings.json","r") as f:
    Dict = json.load(f)
    W = Dict["maxWeight"]
    print(f"W = {W}")
with open("./WeightList.txt","r") as f:
    w = f.readlines()
    w = list(map(int,w))
    print(f"w_items = {len(w)}")

optimalValue = 0
optimalSolution = []

for i in range(0,2**len(w)):
    # decimal 5 -> binary 011
    # In this case, target means [NotUse,Use,Use].
    maxValue = 0
    Solution = []
    target = str(bin(i+2**len(w))).replace("0b1","")
    for j,flag in enumerate(target):
        if flag == "1":
            maxValue += w[j]
            Solution.append(str(j+1))
    if W >= maxValue:
        if maxValue > optimalValue:
            optimalSolution = [Solution]
            optimalValue = maxValue
        elif maxValue == optimalValue:
            optimalSolution.append(Solution)

print(f"optimalValue {optimalValue}")
print(f"optimalSolution {optimalSolution}")