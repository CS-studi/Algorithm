//
//  0234-palindrome-linked-list.swift
//  algo
//
//  Created by MIN SEONG KIM on 2023/03/26.
//

import Foundation


// Definition for singly-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}
 
class Solution {
    func isPalindrome(_ head: ListNode?) -> Bool {
        var slow = head, fast = head, dummy: ListNode? = nil
        
        // reverse first half
        while fast != nil && fast!.next != nil {
            fast = fast!.next!.next
            
            let nextNode = slow!.next
            
            slow!.next = dummy
            
            dummy = slow
            slow = nextNode
        }
        
        // go to the starting point when length of list is odd
        if fast != nil {
            if slow == nil {
                return true
            }
            slow = slow!.next
        }
        
        // compare reversed first and second half
        while slow != nil {
            if slow!.val != dummy!.val {
                return false
            } else {
                slow = slow!.next
                dummy = dummy!.next
            }
        }
        
        return true
    }
}
