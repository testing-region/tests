#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int best[n];
    for (int i; i < n; i++){
        cin >> best[i];
    }

    int bestSum, sum = 0;

    for (int k = 0; k < n; k++) {
       sum = max(best[k], sum+best[k]);
       bestSum = max(bestSum, sum);
    }

    cout << bestSum << '\n';
}
