//
//  Linked_List_Cycle.swift
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


// Floyd's Cycle Finding Algorithm
// 투포인터 사용. 하나는 한 칸씩, 다른 하나는 두 칸씩 이동해 순환이 있다면 반드시 만난다는 사실을 이용
class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        var rear = head
        var front = head?.next

        while front != nil {
            // a === b: a가 참조하고 있는 인스턴스와 b가 참조하고 있는 인스턴스가 같은지 비교
            if rear === front {
                return true
            }

            rear = rear?.next
            front = front?.next?.next
        }

        return false
    }
}
