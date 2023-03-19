
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # unique한 값을 가지는 set 
        unique_node = set()
        
        while head:
            if head in unique_node: # 노드가 전에 이미 돌았던 노드라면 cycle
                return True
            # 처음 보는 노드라면 unique_node 에 추가한다.
            unique_node.add(head)
            head = head.next
        return False
        