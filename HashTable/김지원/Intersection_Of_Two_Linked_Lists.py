def get_length(head):
    list_length = 0
    while head != None:
        head = head.next
        list_length+=1
    return list_length

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length_A= get_length(headA)
        length_B = get_length(headB)
        
        if length_A > length_B:
            curL = headA
            diff = length_A-length_B
            curS = headB
        else:
            curL = headB
            diff = length_B-length_A
            curS = headA
            
        i=0
        while i<diff:
            i+=1
            curL = curL.next
        
        while curL != curS:
            curL = curL.next
            curS = curS.next
        
        return curL
