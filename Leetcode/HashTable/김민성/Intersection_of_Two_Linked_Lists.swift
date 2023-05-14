//
//  Intersection_of_Two_Linked_Lists.swift
//  algo
//
//  Created by MIN SEONG KIM on 2023/03/19.
//

import Foundation


public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}
 
// **(같은 위치에서 시작하게 한 후) 같은 노드를 지날 때 return.
// 더 긴 노드에서 몇 개 노드를 skip할 지 찾기 -> 더 짧은 Linked List의 포인터가 last에 도착하면 더 긴 Linked List의 head로 보낸다.
class Solution {
    func getIntersectionNode(_ headA: ListNode?, _ headB: ListNode?) -> ListNode? {
    
    if headA == nil || headB == nil {
        return nil
    }
    
    var ha: ListNode? = headA
    var hb: ListNode? = headB
    
    while ha !== hb {
        ha = (ha == nil) ? headB : ha?.next
        hb = (hb == nil) ? headA : hb?.next
    }
    
        return ha
    }
}
