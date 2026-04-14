class Solution {
public:
    static long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> mxHeap(gifts.begin(),gifts.end());
        long long sc = 0;
        for (int i = 0; i<k;i++) {
            int temp = floor(sqrt(mxHeap.top()));mxHeap.pop();
            mxHeap.push(temp);
        }
        while (!mxHeap.empty()){sc+=mxHeap.top();mxHeap.pop();}
        return sc;
    }
};