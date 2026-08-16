class Solution {
public:
    int maxSubArray(vector<int>& nums) {

    int maxSum = nums[0];
    int currSum = 0;

    for(int x : nums){
        currSum += x;
        maxSum = max(maxSum, currSum);

        if(currSum < 0)
            currSum = 0;
    }

    return maxSum;
}
};