import random
import json
with open("./Settings.json","r") as f:
    Dict = json.load(f)
    SIZE = Dict["weightListSize"]
    MAX  = Dict["MaxOfItem"]
    MIN  = Dict["MinOfItem"]

a = [str(random.randint(MIN,MAX))+"\n" for i in range(SIZE)]
with open("./WeightList.txt","w") as f:
    f.writelines(a)