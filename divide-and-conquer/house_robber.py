def house_robber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        steal_first = houses[currentIndex] + house_robber(houses, currentIndex + 2)
        steal_second = house_robber(houses, currentIndex + 1)
        return max(steal_first, steal_second)
    
    
houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber(houses, 0))