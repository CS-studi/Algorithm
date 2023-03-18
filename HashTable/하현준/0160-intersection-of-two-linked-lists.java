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
        Set<ListNode> nodes = new HashSet<>();
        while (headA != null || headB != null) {
            if (headA != null) {
                if (nodes.contains(headA))
                    return headA;
                nodes.add(headA);
                headA = headA.next;
            }
            
            if (headB != null) {
                if (nodes.contains(headB))
                    return headB;
                nodes.add(headB);
                headB = headB.next;
            }
        }
        
        return null;
    }
}