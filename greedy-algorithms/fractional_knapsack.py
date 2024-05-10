class Item():
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsack_method(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    used_capacity = 0
    total_value = 0
    
    for i in items:
        if used_capacity + i.weight <= capacity:
            used_capacity += i.weight
            total_value += i.value
        else:
            unused_weight = capacity - used_capacity
            value = i.ratio * unused_weight
            used_capacity += unused_weight
            total_value += value
        if used_capacity == capacity:
            break
    print(f"the total value obtained is {total_value}")
    
item_1 = Item(20, 100)
item_2 = Item(30, 120)
item_3 = Item(10, 60)

custom_list = [item_1, item_2, item_3]

knapsack_method(custom_list, 50)
            
        
    