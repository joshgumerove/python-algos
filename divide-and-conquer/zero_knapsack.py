class Item():
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        

def zero_one_knapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit_1 = items[currentIndex].profit + zero_one_knapsack(items, capacity - items[currentIndex].weight, currentIndex + 1)
        profit_2 = zero_one_knapsack(items, capacity, currentIndex + 1)
        return max(profit_1, profit_2)
    else:
        return 0
    
    
mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(24, 5)

items = [mango, apple, orange, banana]

print(zero_one_knapsack(items, 50, 0))

    