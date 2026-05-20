class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        first_list = []
        second_list = []

        while list1 is not None:
            first_list.append(list1.val)
            list1 = list1.next

        while list2 is not None:
            second_list.append(list2.val)
            list2 = list2.next

        merged_list = sorted(first_list + second_list)

        sorted_linked_list = ListNode(0)
        current_node = sorted_linked_list

        for num in merged_list:
            current_node.next = ListNode(num)
            current_node = current_node.next

        return sorted_linked_list.next
