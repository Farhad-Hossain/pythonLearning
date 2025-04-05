from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to simplify merging process
        current = dummy  # Pointer to construct the new merged list

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move to next node

        # If there are remaining nodes in either list, attach them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next  # The actual head of the merged list

sl = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = sl.mergeTwoLists(l1, l2)

# Print merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")