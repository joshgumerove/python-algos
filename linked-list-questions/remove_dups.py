from linked_list_class import LinkedList
    
#     def remove_dups(self):
#         current_node = self.head
#         values = {current_node.value}
        
#         while current_node.next:
#             if current_node.next.value in values:
#                 current_node.next = current_node.next.next
#             else:
#                 values.add(current_node.next.value)
#                 current_node = current_node.next

def remove_dups(linked_list):
    if linked_list.head is None:
        return 
    else:
        current_node = linked_list.head
        values = {current_node.value}
        while current_node.next:
            if current_node.next.value in values:
                current_node.next = current_node.next.next
            else:
                values.add(current_node.next.value)
                current_node = current_node.next
    return linked_list

def remove_dups1(linked_list):
    if linked_list.head is None:
        return
    current_node = linked_list.head
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next
            
                    
        
first_list = LinkedList()
first_list.generate(5, 0, 10000)
first_list.add(10)
first_list.add(10)
first_list.add(10)
print(first_list)
remove_dups(first_list)
print(first_list)
print("********")
remove_dups1(first_list)
print(first_list)

      
        