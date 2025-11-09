/*Palindrome Number*/
class Solution {
    public boolean isPalindrome(int x) {
        if(x == 0) {
            return true;
        }
        else if(x <= 0) {
            return false;
        }
        else if(x == reverse(x)){
            return true;
        }
        else {
            return false;
        }
    }
    public int reverse(int x) {
        int reverse = 0;
        while (x != 0) {
            reverse = reverse*10 + x%10;
            x = x/10;
        }
        return reverse;
    }
}
