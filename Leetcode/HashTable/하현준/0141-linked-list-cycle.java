/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        int value = Integer.MAX_VALUE;
        while(head != null) {
            if (head.val == Integer.MIN_VALUE) {
                return true;
            }
            head.val = Integer.MIN_VALUE;
            head = head.next;
        }

        return false;
    }
}