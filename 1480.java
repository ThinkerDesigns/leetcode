/*Running Sum of 1d Array*/
class Solution {
    public int[] runningSum(int[] nums) {
        int[] x = new int[nums.length];
        x[0] = nums[0];
        for(int i = 1; i < nums.length; i++) {
            int f = nums[i] + nums[i-1]; 
            x[i] = f;
            nums[i] = x[i];
        }
        return x;
    }
}
