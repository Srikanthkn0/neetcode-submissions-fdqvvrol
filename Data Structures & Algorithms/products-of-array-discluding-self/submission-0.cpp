class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        int i=0;
        while (i<nums.size()){
            int ans=1;
            for(int j=0; j<nums.size(); j++){
                if (i!=j){
                    ans *= nums[j];
                }
            }
            res.push_back(ans);
            i++;
        }
        return res;
    }
};