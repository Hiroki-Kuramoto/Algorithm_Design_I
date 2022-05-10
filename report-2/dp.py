## (start, finish, weight)
## in advance, sorted by "finish" in ascending order
I = [(-1,-1,0),(0,3,1),(2,5,4),(1,6,6),(3,6,2),(4,8,5),(7,10,1),(9,14,7),(12,16,2),(11,17,9),(13,18,3),(15,19,8)]

def main():
    ## 最も最後に終了する要求の終了時刻の長さのリストを作成する
    OPT = [0 for x in range(len(I))]
    for i in range(1,len(I)):
        OPT[i] = max(I[i][2]+OPT[pre(i)],OPT[i-1])
    print(f"optimalValue = {OPT[len(I)-1]}")

    ## 以下では最適値に至る要求の選び方を求める
    OPT_ROOT = [["*"] for x in range(len(I))]
    for i in range(1,len(I)):
        if OPT[i] == I[i][2]+OPT[pre(i)] and OPT[i] == OPT[i-1]:
            OPT_ROOT[i] = OPT_ROOT[i-1] + [x+f"_{I[i]}" for x in OPT_ROOT[pre(i)]]
        elif OPT[i] == I[i][2]+OPT[pre(i)]:
            OPT_ROOT[i] = [x+f"_{I[i]}" for x in OPT_ROOT[pre(i)]]
        elif OPT[i] == OPT[i-1]:
            OPT_ROOT[i] = OPT_ROOT[i-1]
    print(f"optimalSolution = {OPT_ROOT[len(I)-1]}")

def pre(i:int):
    ## i番目の要求が始まる前に最後に終了した要求の番号を返す
    j = i-1
    while(j>0):
        if I[j][1] < I[i][0]:
            return j
        else:
            j -= 1
    return j

if __name__ == "__main__":
    main()