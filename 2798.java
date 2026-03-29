class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int output = 0;
        for (int i = 0;  i < hours.length; i++) {
            if (target <= hours[i]) {
                output += 1;
            }
            else if (target >= hours[i]) {
                output += 0;
            }
        }
        return output;
    }
}
