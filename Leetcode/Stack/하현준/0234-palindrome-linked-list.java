/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;

        // find middle
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next; // slow will be on a middle of the list
        }

        // reverse pointer of second half
        ListNode prev = slow;
        slow = slow.next;
        prev.next = null;
        while (slow != null) {
            ListNode temp = slow.next;
            slow.next = prev; // reverse pointer
            prev = slow; // move pointer
            slow = temp; // move pointer
        }

        // at this point, prev will point to the last node of list
        fast = head;
        slow = prev;
        while (slow != null) {
            if (fast.val != slow.val) {
                return false;
            }
            fast = fast.next;
            slow = slow.next;
        }
        return true;
    }
}