import java.util.HashSet;

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
        // 빈 리스트가 들어 온다면 false 예외 처리
        if(head ==null) return false;
        ListNode slow=head;
        ListNode fast=head;
        
        // prove 노드를 하나 둬, 앞서 탐색한 노드가 천천히 탐색하는 노드와 같게 되면 cycle 존재
        while(fast.next!=null && fast.next.next!=null){
            slow=slow.next; // 한칸씩 이동
            fast=fast.next.next; // 두칸씩 이동
            
            if(slow==fast){
                return true;
            }
        }
        return false;
    }
}