/* 
Frederickson-Lynchのリーダー選挙アルゴリズム
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <math.h>

#define N 10
#define MAXROUND 100

int min(int a, int b) {
    return a < b ? a : b;
}

int main(void) {
    int i;
    int initiater;
    bool hasDone = false;
    int message = -1;
    int ID[10] = {7, 3, 5, 6, 1, 2, 4, 9, 8, 10}; 
    int MIN[10] = {999, 999, 999, 999, 999, 999, 999, 999, 999, 999}; // 最小値を記録する配列
    int RCV[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
    int Delay[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
    bool STATS[10] = {false, false, false, false, false, false, false, false, false, false};

    srand((unsigned)time(NULL));
    initiater = rand() % N;
    printf("initiater: %d\n", initiater);
    
    for(int r=0; r<MAXROUND; r++){
        
        for(int i=0; i<N; i++){
            hasDone = hasDone || STATS[i];
        }
        if (hasDone){
            printf("**************** finished!! ****************\n");
            break;
        }
        
        if (r == 0) {// round 0
            MIN[initiater] = ID[initiater];
            if (initiater+1 < N) {
                RCV[initiater+1] = MIN[initiater];
            } else {
                RCV[0] = ID[initiater];
            }
            Delay[initiater] = 0;
            for(int j=1; j<N; j++){
                i = (initiater+j) % N;
                message = RCV[i];
                RCV[i] = -1;
                MIN[i] = min(message, ID[i]);
                if (i+1 < N) {
                    RCV[i+1] = MIN[i];
                }
                else{
                    RCV[0] = MIN[i];
                }
                Delay[i] = 0;
            }
        }
        else{
            for(int j=0; j<N; j++){
                i = (initiater+j) % N;
                if (STATS[i])
                    continue;
                message = RCV[i];
                RCV[i] = -1;
                if (message == -1) {
                    Delay[i] = Delay[i] + 1;
                }
                else{
                    if (message <= N){
                        // ELECTIONメッセージを受け取った場合
                        if (message == ID[i]){
                            //COORDINATORメッセージを送信し、停止する
                            RCV[i] = N+ID[i];
                            STATS[i] = true;
                        }
                        else if (message < MIN[i]){
                            MIN[i] = message;
                            Delay[i] = 0;
                        }
                        else if (message > MIN[i]){
                            Delay[i] = Delay[i] + 1;
                        }
                    }
                    else{
                        // COORDINATORメッセージを受け取った場合
                        MIN[i] = message-N;
                        if (i+1 < N) {
                            RCV[i+1] = message;
                        }
                        else{
                            RCV[0] = message;
                        }
                        STATS[i] = true;
                    }
                }
                if (Delay[i] == (int)pow(2, MIN[i])){
                    if (i+1 < N) {
                        RCV[i+1] = MIN[i];
                    }
                    else{
                        RCV[0] = MIN[i];
                    }
                }
            }
        }
        printf("Round %d\n", r);
        printf("index\tID\tMIN\tRCV\n");
        for(int i=0; i<N; i++){
            printf("%d\t%d\t%d\t%d\n", i, ID[i], MIN[i], RCV[i]);
        }
    }
    return 0;
}
