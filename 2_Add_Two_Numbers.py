# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def convertToIntegers(cur, list_str):  
            while cur:
                list_str += str(cur.val)
                cur = cur.next
            return list_str
        
        
        def create_linked_list(int_string):
                head = None
                for digit in int_string[::]:
                    node = ListNode(int(digit))
                    node.next = head
                    head = node
                return head
        
        
        cur1 = l1
        cur2 = l2
        l1_str = ""
        l2_str = ""
        x = convertToIntegers(cur1, l1_str)
        y = convertToIntegers(cur2, l2_str)
        x = x[::-1]
        y = y[::-1]
        total = str(int(x) + int(y))
        return create_linked_list(total)

        