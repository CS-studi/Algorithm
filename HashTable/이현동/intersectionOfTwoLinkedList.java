/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null)
            return null;
        ListNode currA = headA;
        ListNode currB = headB;

        while(currA != currB){
            if (currA == null)
                currA = headA;
            else
                currA = currA.next;
            if (currB == null)
                currB = headB;
            else
                currB = currB.next;
        }
        return currA;

    }
}