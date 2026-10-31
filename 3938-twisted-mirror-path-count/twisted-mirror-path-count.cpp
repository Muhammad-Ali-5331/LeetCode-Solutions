#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.precision(10);

// The macro to mimic print(*arr)
#define print_v(v) for(auto _i=0; _i<v.size(); ++_i) std::cout << v[_i] << (_i==v.size()-1 ? "" : " "); std::cout << endl;

class Solution {
public:
    ll R, C;
    ll MOD = 1e9 + 7;
    int uniquePaths(vector<vector<int>>& grid) {
        R = grid.size();
        C = grid[0].size();
        vector<vector<vector<ll>>> dp(R, vector<vector<ll>>(C, vector<ll>(2, 0)));
        dp[0][0][0] = 1;
        for(int i = 1; i<C; i++){
            dp[0][i][0] += (dp[0][i-1][0] + dp[0][i-1][1])%MOD;
            if (grid[0][i] == 1) break;
        }
        for(int i = 1; i<R; i++){
            dp[i][0][1] += (dp[i-1][0][0] + dp[i-1][0][1]) % MOD;
            if (grid[i][0] == 1) break;
        }
        for (int r = 1; r<R; r++){
            for (int c = 1; c<C; c++){
                
                // Calculate Left paths
                if (grid[r][c-1] == 0) dp[r][c][0]+= (dp[r][c-1][0] + dp[r][c-1][1])%MOD;
                else dp[r][c][0] += dp[r][c-1][1] % MOD;

                // Calcualte Right paths
                if (grid[r-1][c] == 0) dp[r][c][1] += (dp[r-1][c][0] + dp[r-1][c][1])%MOD;
                else dp[r][c][1] += dp[r-1][c][0] % MOD;

            }
        }
        return (dp[R-1][C-1][0] + dp[R-1][C-1][1]) % MOD;
    }
};