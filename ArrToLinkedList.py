class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def array_to_linked_list(arr):
    if not arr:  # If the array is empty, return None
        return None

    # Create the head node of the linked list
    head = ListNode(arr[0])
    current = head

    # Iterate through the array and link nodes together
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# Helper function to print the linked list (for testing)
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))


# Example Usage
array = [1, 2, 3, 4, 5, 6]
linked_list = array_to_linked_list(array)
print_linked_list(linked_list)
