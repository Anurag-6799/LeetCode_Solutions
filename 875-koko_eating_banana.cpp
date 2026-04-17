class Solution {
public:
    long long calculating_hours(vector<int>&pile, int k){
        long long count=0;
        for(auto &i:pile){
            if(i<=k) count++;
            else{
                int r = i%k;
                count+=(i/k);
                if(r){
                    count++;
                }
            }
        }
        return count;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int left=1, right;
        for(auto &i:piles){
            right=max(i,right);
        }
        long long ans = right;
        while(left<=right){
            long long mid=left+(right-left)/2;
            long long no_hr = calculating_hours(piles, mid);
            // cout<<"nohr - "<<no_hr<<endl;               
            if(no_hr==h){
                // cout<<"mid- "<<mid<<endl;
                ans=min(ans, mid);
                right=mid-1;
            }
            else if(no_hr>h){
                left=mid+1;
            }
            else {
                ans = min(ans,mid);
                right=mid-1;
            }
        }
        return ans;
    }
};