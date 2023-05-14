/*
 * @lc app=leetcode id=387 lang=java
 *
 * [387] First Unique Character in a String
 */

// @lc code=start
class Solution {
    public int firstUniqChar(String s) {
        int[] data = new int[36];
        for (int i = 0; i < s.length(); i++) {
            data[s.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < s.length(); i++) {
            if (data[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }

        return -1;
    }
}
// @lc code=end
